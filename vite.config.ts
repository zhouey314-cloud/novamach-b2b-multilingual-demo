import { defineConfig,loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig(({mode})=>{
  const env=loadEnv(mode,'.','')
  const vercelDomain=env.VERCEL_PROJECT_PRODUCTION_URL||env.VERCEL_URL
  const siteUrl=env.VITE_SITE_URL||(vercelDomain?`https://${vercelDomain}`:'')
  return {
    plugins:[react()],
    define:{'import.meta.env.VITE_SITE_URL':JSON.stringify(siteUrl)},
  }
})
