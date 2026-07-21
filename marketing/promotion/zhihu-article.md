# 我花了一周时间，用FastAPI做了一个AI写作工具，现在把它开源了

自从ChatGPT出来之后，AI写作工具层出不穷。但大部分都是SaaS服务，按月收费，数据还不在自己手里。

作为一个开发者，我就想：能不能自己搭一个？

于是花了大概一周时间，做了 **AI Content Studio**。

## 这个东西能干什么

它就是一个完整的AI内容生成平台：

**6种内容类型：**
- 博客文章 - 带标题层级和SEO的完整文章
- 社交媒体 - 针对不同平台优化的帖子
- 广告文案 - 转化导向的广告语
- 邮件营销 - 专业的营销邮件
- SEO内容 - 搜索优化的内容
- 自定义 - 你想要什么就写什么

**完整的用户系统：**
- 注册/登录（JWT认证）
- 免费用户送5次积分
- Pro用户每月100次积分
- API密钥管理

**最关键的：带支付系统**
接入了Stripe，用户可以直接用信用卡订阅Pro，$19.99/月。如果你部署上线，就是一个可以直接收钱的SaaS。

## 技术栈

- 后端：FastAPI（Python）
- 数据库：SQLAlchemy + SQLite/PostgreSQL
- 前端：Vanilla JS + CSS（零依赖）
- 支付：Stripe
- AI：OpenAI API
- 部署：Docker + nginx

## 为什么要自己做

市面上的AI写作工具，一个月动不动就$29、$49。而且：

1. **数据安全** - 你的数据在别人服务器上
2. **不可定制** - 功能是别人定的，你改不了
3. **长期成本** - 按月付费，一年下来不少钱

自己部署一个，所有数据在自己手里，想改什么改什么。

## 怎么用

本地运行：

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

打开 http://localhost:8000 就能用。不需要API Key也能体验Demo模式。

Docker部署：

```bash
docker compose up -d
```

## 怎么收钱

接入Stripe，填两个密钥就行：

```
STRIPE_SECRET_KEY=sk_live_xxx
STRIPE_PUBLISHABLE_KEY=pk_live_xxx
```

用户点"Upgrade to Pro"，走Stripe Checkout流程，钱直接到你Stripe账户。

## 源码

源码放在Gumroad上，包含完整的后端+前端+Docker配置+安装文档。

https://gumroad.com（这里放你的链接）

价格$49。一次购买，永久使用，可以商用。

## 写在最后

这一周从零搭了这个平台，所有功能都是实际可用的。如果你正好需要一个AI写作工具，不管是自己用还是拿来赚钱，它都能帮你省下大量时间。

有什么问题评论区见。
