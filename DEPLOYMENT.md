# 部署说明

## Vercel（推荐）

V1.1 已完成正式预览部署：<https://0-1-b2b-demo-demo-novamach.vercel.app>。

后续重新部署可在项目根目录执行：

```bash
npx vercel deploy --prod -y --build-env VITE_ALLOW_INDEXING=false
```

构建会自动读取 Vercel 提供的实际域名作为 `VITE_SITE_URL`。根目录 `vercel.json` 已配置 SPA 路由回退；虚构 Demo 保持全站 `noindex,nofollow`。

## Netlify

1. 导入仓库。
2. Build Command：`pnpm build`。
3. Publish Directory：`dist`。
4. `public/_redirects` 已配置 SPA 回退。

## 任意静态托管 / Nginx

运行 `pnpm build` 后上传 `dist/`。服务器需将不存在的文件路径回退至 `/index.html`，否则产品详情和 `/admin-demo` 刷新时会 404。

Nginx 核心规则：

```nginx
location / {
  try_files $uri $uri/ /index.html;
}
```

## 上线前必做

- 将 `demo.example.com` 替换为正式域名
- 设置 `VITE_SITE_URL`；构建会据此生成页面地址、sitemap 与 robots 的基础地址
- NovaMach 是虚构品牌，预览部署必须保持 `VITE_ALLOW_INDEXING=false`；此时页面为 `noindex,nofollow`，`robots.txt` 阻止全站抓取
- 只有品牌、企业信息、产品、参数、案例、认证和联系方式均已替换并经人工核验，才可设置 `VITE_ALLOW_INDEXING=true`
- `/admin-demo` 始终 `noindex,nofollow` 且不进入 sitemap；客户能力卡与客户介绍页也不进入 sitemap
- 接入真实 RFQ 接口并增加隐私政策、反垃圾与服务器端校验
- 替换 WhatsApp 企业号码与示例邮箱；产品手册统一使用 `/brochure`
- 对公司信息、参数、案例、证书和文章进行人工事实审核
- 如不再是 Demo，必须重新评估免责声明；在此之前请勿删除 Demo 标识
- 为三语 SEO 设计独立 URL 与 `hreflang`，并从 CMS 生成完整 sitemap
