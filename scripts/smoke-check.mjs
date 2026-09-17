import {access,readFile} from 'node:fs/promises'

const required=['dist/index.html','dist/robots.txt','dist/sitemap.xml','dist/assets/og-image.jpg','dist/assets/hero-factory.png','dist/assets/product-sprite.png']
for(const file of required)await readFile(file)
const html=await readFile('dist/index.html','utf8')
for(const marker of ['canonical','og:image','twitter:card','demo-schema','noindex,nofollow'])if(!html.includes(marker))throw new Error(`Missing ${marker} in production HTML`)
const sitemap=await readFile('dist/sitemap.xml','utf8')
if(sitemap.includes('/admin-demo'))throw new Error('Admin demo must not appear in sitemap')
const robots=await readFile('dist/robots.txt','utf8')
if(!robots.includes('Disallow: /'))throw new Error('Fictional demo must default to blocked indexing')
try{await access('dist/novamach-demo-brochure.txt');throw new Error('Legacy brochure text file still exists')}catch(error){if(error instanceof Error&&error.message.includes('Legacy'))throw error}
console.log(`Smoke artifacts PASS (${required.length} required files, noindex policy and SEO boundaries present)`)
