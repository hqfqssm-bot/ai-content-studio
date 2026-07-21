# AI Content Studio - Complete AI Content Generation SaaS

**A production-ready AI-powered content generation platform. Built with FastAPI + vanilla JS, ready to deploy as a SaaS or sell as source code.**

## Key Features

- **User Authentication** — JWT-based register/login with bcrypt password hashing
- **AI Content Generation** — Blog posts, social media, ads, emails, SEO content, custom
- **Credit System** — Free tier (5 credits) + Pro tier (100 credits/month)
- **Payment Integration** — Stripe Checkout subscription for Pro upgrades
- **API Key Management** — Generate and manage API keys for external integrations
- **Content History** — Browse and reuse past generations
- **Demo Mode** — Works without an API key for testing
- **Mobile Responsive** — Works on all devices
- **Docker Ready** — One-command deploy with PostgreSQL + nginx

## Quick Start

### Local (requires Python 3.10+)
```
cd backend
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
Open http://localhost:8000

### Docker (production)
```
docker compose up -d
```
Open http://localhost

### Windows (one-click)
Double-click `start.bat`

## Required Configuration

| Variable | Required | Description |
|----------|----------|-------------|
| OPENAI_API_KEY | Yes | OpenAI API key for AI content generation |
| STRIPE_SECRET_KEY | No | Stripe secret key (for Pro subscription payments) |
| STRIPE_PUBLISHABLE_KEY | No | Stripe publishable key |
| SECRET_KEY | Yes | JWT signing secret (change in production) |

## Monetization (This is the important part)

### Option A: Sell the Source Code
| Platform | Price Range | Notes |
|----------|------------|-------|
| CodeCanyon | $49-199 | Package as a complete product |
| Gumroad | $29-149 | Direct sales with deployment guide |
| 微信/技术社群 | 500-2000 yuan | Sell to Chinese developers |
| 闲鱼/淘宝 | 200-500 yuan | Volume sales |

### Option B: Deploy as SaaS
1. Buy a domain ($10-15/yr)
2. Deploy to VPS (Railway / Fly.io / 阿里云)
3. Set your Stripe keys in .env
4. Start charging $19.99/month for Pro

| Users | Monthly Revenue |
|-------|----------------|
| 10 Pro users | $200/month |
| 50 Pro users | $1,000/month |
| 100 Pro users | $2,000/month |

### Option C: Freelance / Custom Builds
Use this as a demo to win contracts:
- Enterprise AI content platform: 3,000-10,000 yuan/project
- Custom development: 5,000-20,000 yuan/project
- Monthly maintenance: 1,000-3,000 yuan/month

### Option D: Content Monetization
1. Deploy the public version
2. Create tutorials on Zhihu / Bilibili / YouTube
3. Drive traffic to your platform, convert free users to Pro

## Tech Stack
Backend: FastAPI | Database: SQLAlchemy + SQLite/PostgreSQL | Auth: JWT + bcrypt | AI: OpenAI API | Payments: Stripe | Frontend: Vanilla JS + CSS | Deployment: Docker + nginx

## License
MIT - free to use, modify, and sell.
