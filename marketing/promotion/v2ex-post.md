出一套 AI Content Studio 源码 - 完整的AI内容生成平台

自己用 FastAPI 开发的一个 AI 写作 SaaS 平台，现在打包出售源码。

功能：
- JWT 注册/登录
- 6 种 AI 内容生成（博客/社交媒体/广告/邮件/SEO/自定义）
- 积分系统（免费5次，Pro 100次/月）
- Stripe 支付集成（收钱的，不是摆设）
- API Key 管理
- 内容历史
- Docker 一键部署（nginx + PostgreSQL）

技术栈：FastAPI + SQLAlchemy + Vanilla JS + Stripe + OpenAI

本地跑：pip install -r requirements.txt && uvicorn app.main:app --reload
上线跑：docker compose up -d

买回去你可以：
1. 自己部署用
2. 改一改卖给客户
3. 当 SaaS 上线收月费

Gumroad 链接：https://gumroad.com（你的链接）
定价 $49

支持定制开发，有想法的可以联系。
