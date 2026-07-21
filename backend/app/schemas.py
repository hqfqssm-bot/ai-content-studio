from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


# ---------- Auth ----------
class UserRegister(BaseModel):
    email: str
    password: str
    name: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: "UserResponse"


class UserResponse(BaseModel):
    id: str
    email: str
    name: Optional[str] = None
    credits: int = 0
    is_pro: bool = False
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ---------- Content ----------
class GenerateRequest(BaseModel):
    content_type: str  # blog, social, ad, email, seo, custom
    prompt: str
    tone: Optional[str] = "professional"
    language: Optional[str] = "zh-CN"
    max_tokens: Optional[int] = 1000


class GenerateResponse(BaseModel):
    id: str
    content: str
    content_type: str
    tokens_used: int
    credits_used: int
    created_at: datetime


# ---------- API Keys ----------
class ApiKeyCreate(BaseModel):
    name: Optional[str] = None


class ApiKeyResponse(BaseModel):
    id: str
    key: str
    name: Optional[str] = None
    is_active: bool
    created_at: datetime
    last_used_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# ---------- Generic ----------
class MessageResponse(BaseModel):
    message: str


class CreditResponse(BaseModel):
    credits: int
