# NovaMach 工业站 Demo — 中文简历项目要点

仅描述公开仓库内可核查的自建演示；按岗位挑选，勿三版叠加。证据与边界以 README、测试和 [case study](case-study.md) 为准。

## AI Engineer / FDE

- 围绕“B2B 外贸站要完整展示产品到 RFQ 路径，又不能虚构真实企业背书”，用 React、TypeScript、Vite、Vercel 实现三语产品/内容、多路由、RFQ 到演示后台的本地闭环、响应式和默认 noindex。
- 验证：lint/typecheck/build/smoke 及线上桌面/移动、直达路由和样本 RFQ 检查；运行时无生成式 AI；测试集中在站点功能和内容边界。
- 明确边界：品牌、产品、认证、案例、询盘全是样本；RFQ 不会发送到服务器。

## AI Product / Solution

- 将“B2B 外贸站要完整展示产品到 RFQ 路径，又不能虚构真实企业背书”拆成可点击的用户流程，交付三语产品/内容、多路由、RFQ 到演示后台的本地闭环、响应式和默认 noindex。
- 用可运行 Demo、测试和案例页说明实现与限制；lint/typecheck/build/smoke 及线上桌面/移动、直达路由和样本 RFQ 检查。
- 为客户化落地列出前置条件：客户审核真实文案/图片、接入安全询盘端点与后台权限后再开放索引。

## 实习 / 校招

- 独立完成NovaMach 工业站 Demo的公开演示、代码、测试和文档，技术栈为 React、TypeScript、Vite、Vercel。
- 解决“让三语言、移动端及虚构声明同时保持一致”，保留可复核的验证：lint/typecheck/build/smoke 及线上桌面/移动、直达路由和样本 RFQ 检查。
- 不把演示包装成上线业务：品牌、产品、认证、案例、询盘全是样本；RFQ 不会发送到服务器。
