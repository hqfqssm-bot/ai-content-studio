<div align="center">

# AI Content Studio · AI 内容创作平台

**基于 FastAPI 的 AI 内容生成 SaaS 系统，含 Stripe 支付、JWT 认证、Docker 部署**

[在线演示](https://hqfqssm-bot.github.io/ai-content-studio) | [购买](https://hqfqssm.gumroad.com/l/zofcdb)

</div>

## 项目简介

AI Content Studio 是一个完整的 AI 内容生成平台，支持 6 种内容类型，内置用户系统、积分体系和 Stripe 支付。

可用于：部署为 SaaS 服务收费、二次开发、学习 FastAPI+Stripe 集成

## 功能特性

- **JWT 注册/登录** — 安全的 bcrypt 密码加密
- **6 种内容类型** — 博客、社交媒体、广告、邮件、SEO、自定义
- **积分系统** — 免费 5 次，Pro 100 次/月
- **Stripe 支付** — Checkout 订阅，$19.9/月
- **API 密钥管理** — Pro 用户可创建/删除 API Key
- **Docker 部署** — 一行命令部署，含 nginx + PostgreSQL
- **Demo 模式** — 无需 API Key 即可测试

## 快速开始

```bash
# 进入后端目录，安装依赖
cd backend
pip install -r requirements.txt

# 配置 .env（复制 .env.example 并填入密钥）

# 启动
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

打开 http://localhost:8000

Docker 部署：
```bash
docker compose up -d
```

## API 接口

POST /api/auth/register — 注册
POST /api/auth/login — 登录
POST /api/content/generate — 生成内容
POST /api/payments/create-checkout-session — Stripe 订阅
GET /api/keys/ — 列出 API Key

## 购买完整源码

➡️ https://hqfqssm.gumroad.com/l/zofcdb
价格：$19.9 — 永久使用，可商用
