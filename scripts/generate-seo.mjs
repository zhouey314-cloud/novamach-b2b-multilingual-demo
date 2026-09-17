import {writeFile} from 'node:fs/promises'

const vercelDomain=process.env.VERCEL_PROJECT_PRODUCTION_URL||process.env.VERCEL_URL
const siteUrl=(process.env.VITE_SITE_URL||(vercelDomain?`https://${vercelDomain}`:'https://novamach-demo.example')).replace(/\/$/,'')
const allowIndexing=process.env.VITE_ALLOW_INDEXING==='true'
const routes=['/','/products','/products/nx-500-five-axis','/solutions','/cases','/about','/news','/contact','/brochure']
const urls=routes.map(route=>`  <url><loc>${siteUrl}${route}</loc></url>`).join('\n')
const sitemap=`<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`
const robots=allowIndexing
  ? `User-agent: *\nAllow: /\nDisallow: /admin-demo\nDisallow: /capability-card\nDisallow: /customer-deck\nSitemap: ${siteUrl}/sitemap.xml\n`
  : `# Fictional demonstration brand — indexing disabled by default.\nUser-agent: *\nDisallow: /\n`
await Promise.all([writeFile('public/sitemap.xml',sitemap),writeFile('public/robots.txt',robots)])
console.log(`Generated SEO files for ${siteUrl} (${allowIndexing?'indexing enabled':'demo noindex default'})`)
