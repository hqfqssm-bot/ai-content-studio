# 一键发布到 GitHub

准备工作：需要一个 GitHub 账号（免费），没有的话先去 github.com 注册。

## 第 1 步：在 GitHub 创建仓库

1. 打开 https://github.com/new
2. Repository name 填：`ai-content-studio`
3. Description 填：`AI-powered content generation platform - FastAPI + Stripe + JWT auth`
4. 选 Public（公开）
5. 不要勾 "Initialize this repository with a README"
6. 点 Create repository

## 第 2 步：推送代码

GitHub 创建完后会显示一个页面，里面有几行命令。复制下面这整段代码，粘贴到 PowerShell 里运行：

```powershell
cd C:\Users\41896\Documents\11
git init
git add .
git commit -m "Initial commit: AI Content Studio v1.0"
git remote add origin https://github.com/你的用户名/ai-content-studio.git
git branch -M main
git push -u origin main
```

（把 `你的用户名` 替换成你的 GitHub 用户名）

## 第 3 步：开启 GitHub Pages

1. 打开 https://github.com/你的用户名/ai-content-studio/settings/pages
2. Source 选 "Deploy from a branch"
3. Branch 选 `main`，文件夹选 `/docs`
4. 点 Save
5. 等 2 分钟，你的产品展示页就在：`https://你的用户名.github.io/ai-content-studio`

## 第 4 步：更新你的 Gumroad 链接

把这个 GitHub Pages 地址填进你的 Gumroad 产品描述里，买家可以预览产品功能再决定购买。

## 完成效果

- GitHub 仓库：`github.com/你的用户名/ai-content-studio` ← 开发者搜索到这里，看到代码质量决定购买
- 产品展示页：`你的用户名.github.io/ai-content-studio` ← 发帖子时直接甩这个链接
- Gumroad：卖源码收钱
