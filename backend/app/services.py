import logging
from functools import lru_cache
from typing import Optional

from openai import OpenAI

from .config import settings

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def get_openai_client() -> Optional[OpenAI]:
    if not settings.OPENAI_API_KEY:
        logger.warning("No OPENAI_API_KEY set; using demo mode")
        return None
    return OpenAI(
        api_key=settings.OPENAI_API_KEY,
        base_url=settings.OPENAI_BASE_URL,
    )


CONTENT_PROMPTS = {
    "blog": (
        "You are a professional blogger. Write a well-structured blog post "
        "with headings, paragraphs, and engaging introduction and conclusion. "
        "Use markdown formatting. "
    ),
    "social": (
        "You are a social media content creator. Write engaging social media posts "
        "optimized for the given platform. Include relevant hashtags. "
    ),
    "ad": (
        "You are a copywriter specializing in advertising. Write compelling ad copy "
        "that drives conversions. Include a headline, body, and call-to-action. "
    ),
    "email": (
        "You are an email marketing specialist. Write a professional marketing email "
        "with subject line, greeting, body, and signature. "
    ),
    "seo": (
        "You are an SEO content strategist. Write SEO-optimized content including "
        "meta title, meta description, keyword-rich body, and heading structure. "
    ),
    "custom": (
        "You are a versatile content creator. Write high-quality content based on the user's request. "
    ),
}


def get_system_prompt(content_type: str, tone: str, language: str) -> str:
    base = CONTENT_PROMPTS.get(content_type, CONTENT_PROMPTS["custom"])
    tone_guide = f"Use a {tone} tone."
    lang_guide = f"Write the content in {language}."
    return f"{base}\n{tone_guide}\n{lang_guide}"


def generate_content(
    content_type: str,
    prompt: str,
    tone: str = "professional",
    language: str = "zh-CN",
    max_tokens: int = 1000,
) -> tuple[str, int]:
    client = get_openai_client()
    if client is None:
        raise RuntimeError("OpenAI API key not configured")

    system_prompt = get_system_prompt(content_type, tone, language)

    response = client.chat.completions.create(
        model=settings.DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        temperature=0.7,
    )

    content = response.choices[0].message.content or ""
    tokens_used = response.usage.total_tokens if response.usage else 0

    return content, tokens_used
