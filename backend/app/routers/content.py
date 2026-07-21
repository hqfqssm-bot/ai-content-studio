from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User, Generation
from ..schemas import GenerateRequest, GenerateResponse
from ..auth import get_current_user
from ..services import generate_content
from ..config import settings

router = APIRouter(prefix="/api/content", tags=["content"])

COST_PER_GENERATION = 1


@router.post("/generate", response_model=GenerateResponse)
def generate(
    data: GenerateRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if user.credits < COST_PER_GENERATION:
        raise HTTPException(
            status_code=402,
            detail="Insufficient credits. Please purchase more credits.",
        )

    if not settings.OPENAI_API_KEY:
        content = (
            f"# {data.content_type.title()} Content\n\n"
            f"*Demo mode - this is sample output.*\n\n"
            f"**Your prompt:** {data.prompt}\n\n"
            f"**Tone:** {data.tone}\n"
            f"**Language:** {data.language}\n\n"
            f"---\n\n"
            f"This is a placeholder. To generate real AI content, "
            f"set OPENAI_API_KEY in your .env file."
        )
        tokens_used = 0
    else:
        try:
            content, tokens_used = generate_content(
                content_type=data.content_type,
                prompt=data.prompt,
                tone=data.tone,
                language=data.language,
                max_tokens=data.max_tokens,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"AI generation failed: {str(e)}")

    user.credits -= COST_PER_GENERATION

    generation = Generation(
        user_id=user.id,
        content_type=data.content_type,
        prompt=data.prompt,
        result=content,
        tokens_used=tokens_used,
    )
    db.add(generation)
    db.commit()
    db.refresh(generation)

    return GenerateResponse(
        id=generation.id,
        content=content,
        content_type=data.content_type,
        tokens_used=tokens_used,
        credits_used=COST_PER_GENERATION,
        created_at=generation.created_at,
    )


@router.get("/history", response_model=list[GenerateResponse])
def get_history(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    gens = (
        db.query(Generation)
        .filter(Generation.user_id == user.id)
        .order_by(Generation.created_at.desc())
        .limit(50)
        .all()
    )
    return [
        GenerateResponse(
            id=g.id,
            content=g.result or "",
            content_type=g.content_type,
            tokens_used=g.tokens_used,
            credits_used=COST_PER_GENERATION,
            created_at=g.created_at,
        )
        for g in gens
    ]


@router.get("/types")
def get_content_types():
    return {
        "types": [
            {"id": "blog", "name": "Blog Post", "icon": "file-text", "description": "Well-structured blog articles with headings and SEO"},
            {"id": "social", "name": "Social Media", "icon": "share2", "description": "Posts optimized for social platforms"},
            {"id": "ad", "name": "Advertisement", "icon": "trending-up", "description": "Conversion-focused ad copy"},
            {"id": "email", "name": "Email Marketing", "icon": "mail", "description": "Professional marketing emails"},
            {"id": "seo", "name": "SEO Content", "icon": "search", "description": "Search engine optimized content"},
            {"id": "custom", "name": "Custom", "icon": "edit-3", "description": "Any custom content you need"},
        ]
    }


@router.get("/pricing")
def get_pricing():
    return {
        "free": {"credits": settings.FREE_CREDITS, "price": 0},
        "pro": {"credits": settings.PRO_CREDITS, "price_monthly": settings.PRO_PRICE_MONTHLY},
        "cost_per_generation": COST_PER_GENERATION,
        "currency": "USD",
    }
