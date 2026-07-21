
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import secrets

from ..database import get_db
from ..models import User, ApiKey
from ..schemas import ApiKeyCreate, ApiKeyResponse, MessageResponse
from ..auth import get_current_user

router = APIRouter(prefix="/api/keys", tags=["api_keys"])


@router.get("/", response_model=list[ApiKeyResponse])
def list_keys(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    keys = db.query(ApiKey).filter(ApiKey.user_id == user.id).order_by(ApiKey.created_at.desc()).all()
    return keys


@router.post("/", response_model=ApiKeyResponse)
def create_key(data: ApiKeyCreate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if not user.is_pro:
        raise HTTPException(status_code=403, detail="Only Pro users can create API keys")
    raw_key = "acs_" + secrets.token_hex(24)
    key = ApiKey(
        user_id=user.id,
        key=raw_key,
        name=data.name or "Unnamed Key",
    )
    db.add(key)
    db.commit()
    db.refresh(key)
    return key


@router.delete("/{key_id}", response_model=MessageResponse)
def delete_key(key_id: str, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    key = db.query(ApiKey).filter(ApiKey.id == key_id, ApiKey.user_id == user.id).first()
    if not key:
        raise HTTPException(status_code=404, detail="API key not found")
    db.delete(key)
    db.commit()
    return {"message": "API key deleted"}
