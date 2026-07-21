# 发布到 Gitee（码云）— 国内开发者平台

Gitee 是中国的 GitHub，国内开发者经常在上面找开源项目。

## 为什么重要
- 国内开发者访问 GitHub 可能慢
- Gitee 在百度等搜索引擎排名好
- 可以直接在 Gitee 上卖源码（Gitee 有付费下载功能）

## 步骤

1. 打开 https://gitee.com 注册账号
2. 点右上角 "+" → 新建仓库
3. 仓库名填 `ai-content-studio`
4. 选公开
5. 创建后，在本地运行：

```powershell
cd C:\Users\41896\Documents\11
git remote add gitee https://gitee.com/你的用户名/ai-content-studio.git
git push -u gitee main
```

## 在 Gitee 上卖源码

Gitee 有 "付费下载" 功能，可以直接在仓库页面开启：
1. 进入仓库 → 管理 → 仓库设置
2. 开启 "付费下载"
3. 设置价格（建议 ¥29-99）
4. 用户付费后才能下载源码
