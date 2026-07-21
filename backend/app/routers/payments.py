
import logging
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User
from ..auth import get_current_user
from ..config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/payments", tags=["payments"])

stripe = None
_stripe_initialized = False


def get_stripe():
    global stripe, _stripe_initialized
    if not _stripe_initialized:
        if settings.STRIPE_SECRET_KEY:
            try:
                import stripe as _stripe
                _stripe.api_key = settings.STRIPE_SECRET_KEY
                stripe = _stripe
                logger.info("Stripe initialized")
            except ImportError:
                logger.warning("stripe package not installed")
        else:
            logger.info("Stripe not configured (no STRIPE_SECRET_KEY)")
        _stripe_initialized = True
    return stripe


@router.get("/config")
def get_config():
    s = get_stripe()
    return {
        "stripe_configured": s is not None,
        "publishable_key": settings.STRIPE_PUBLISHABLE_KEY or "",
        "pro_price": settings.PRO_PRICE_MONTHLY,
        "pro_credits": settings.PRO_CREDITS,
        "currency": "USD",
    }


@router.post("/create-checkout-session")
def create_checkout_session(user: User = Depends(get_current_user)):
    s = get_stripe()
    if not s:
        raise HTTPException(status_code=503, detail="Payment system not configured. Set STRIPE_SECRET_KEY in .env")

    try:
        session = s.checkout.Session.create(
            mode="subscription",
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "AI Content Studio Pro"},
                    "recurring": {"interval": "month"},
                    "unit_amount": int(settings.PRO_PRICE_MONTHLY * 100),
                },
                "quantity": 1,
            }],
            metadata={"user_id": user.id},
            success_url=settings.FRONTEND_URL + "?payment=success",
            cancel_url=settings.FRONTEND_URL + "?payment=canceled",
        )
        return {"url": session.url, "session_id": session.id}
    except Exception as e:
        logger.error(f"Stripe checkout failed: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to create checkout session: {str(e)}")


@router.post("/webhook")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):
    s = get_stripe()
    if not s:
        raise HTTPException(status_code=503, detail="Stripe not configured")

    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    if not sig_header:
        raise HTTPException(status_code=400, detail="Missing stripe-signature header")

    try:
        event = s.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except s.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        user_id = session.get("metadata", {}).get("user_id")
        if user_id:
            user = db.query(User).filter(User.id == user_id).first()
            if user:
                user.is_pro = True
                user.credits += settings.PRO_CREDITS
                db.commit()
                logger.info(f"User {user_id} upgraded to Pro")

    return {"status": "ok"}


@router.post("/verify-pro")
def verify_pro_status(user: User = Depends(get_current_user)):
    return {"is_pro": user.is_pro, "credits": user.credits}
