# Architecture

NovaMach is a client-side React/Vite demonstration site.

```text
src/content.ts  synthetic content and translations
src/App.tsx     route selection, pages, RFQ and admin-demo interactions
src/demoStore.ts localStorage-backed demo state
src/styles.css  responsive presentation system
public/assets/  unbranded visual assets
scripts/        SEO generation and smoke checks
```

The RFQ and `/admin-demo` flows use browser-local state only. There is no
server, database, authentication layer, CRM integration or message delivery.
