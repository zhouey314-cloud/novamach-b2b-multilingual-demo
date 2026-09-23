import type {Lang,LocalText,Product} from './content'

export type InquiryStatus='New'|'Contacted'|'Qualified'
export type DemoInquiry={id:string;name:string;company:string;email:string;market:string;product:string;requirements:string;createdAt:string;status:InquiryStatus}
export type ProductOverride={slug:string;name:string;category:string;status:'Published'|'Draft';description:string}
export type ArticleOverride={index:number;title:string;excerpt:string;status:'Published'|'Draft'}
export type SeoSettings={siteTitle:string;description:string;canonical:string}

const KEYS={inquiries:'novamach-demo-inquiries',products:'novamach-demo-products',articles:'novamach-demo-articles',seo:'novamach-demo-seo'} as const

export const defaultInquiries:DemoInquiry[]=[
  {id:'RFQ-1024',name:'Sample Buyer 01',company:'Example Metalworks',email:'buyer01@example.com',market:'Spain',product:'LF-3015 Fiber Laser',requirements:'Sample request for sheet-metal cutting capacity and delivery scope.',createdAt:'2026-08-30T09:24:00.000Z',status:'New'},
  {id:'RFQ-1023',name:'Sample Buyer 02',company:'Demo Components GmbH',email:'buyer02@example.com',market:'Germany',product:'NX-500 Five-Axis Center',requirements:'Sample inquiry for a compact precision machining cell.',createdAt:'2026-08-29T14:10:00.000Z',status:'Contacted'},
  {id:'RFQ-1022',name:'Sample Buyer 03',company:'Example Packaging Ltd.',email:'buyer03@example.com',market:'Brazil',product:'PK-60 Packaging Line',requirements:'Sample end-of-line packaging workflow request.',createdAt:'2026-08-28T08:42:00.000Z',status:'Qualified'},
]

export const defaultSeo:SeoSettings={siteTitle:'NovaMach Industrial | Precision Equipment Demo',description:'Sample multilingual B2B machinery website for sales demonstration.',canonical:'https://0-1-b2b-demo-demo-novamach.vercel.app'}

function read<T>(key:string,fallback:T):T{try{const value=localStorage.getItem(key);return value?JSON.parse(value) as T:fallback}catch{return fallback}}
function write<T>(key:string,value:T){localStorage.setItem(key,JSON.stringify(value));window.dispatchEvent(new Event('novamach-demo-updated'))}

export const getInquiries=()=>read<DemoInquiry[]>(KEYS.inquiries,defaultInquiries)
export const saveInquiry=(value:DemoInquiry)=>write(KEYS.inquiries,[value,...getInquiries()])
export const updateInquiryStatus=(id:string,status:InquiryStatus)=>write(KEYS.inquiries,getInquiries().map(item=>item.id===id?{...item,status}:item))
export const deleteInquiry=(id:string)=>write(KEYS.inquiries,getInquiries().filter(item=>item.id!==id))

export const getProductOverrides=()=>read<ProductOverride[]>(KEYS.products,[])
export const saveProductOverride=(value:ProductOverride)=>write(KEYS.products,[...getProductOverrides().filter(item=>item.slug!==value.slug),value])
export const getDemoProducts=(base:Product[]):Array<Product&{demoStatus:'Published'|'Draft'}>=>{const overrides=getProductOverrides();return base.map(product=>{const override=overrides.find(item=>item.slug===product.slug);if(!override)return {...product,demoStatus:'Published'};const replaceEn=(value:LocalText,en:string):LocalText=>({...value,en});return {...product,name:replaceEn(product.name,override.name),category:replaceEn(product.category,override.category),description:replaceEn(product.description,override.description),demoStatus:override.status}})}

export const getArticleOverrides=()=>read<ArticleOverride[]>(KEYS.articles,[])
export const saveArticleOverride=(value:ArticleOverride)=>write(KEYS.articles,[...getArticleOverrides().filter(item=>item.index!==value.index),value])
export const getDemoArticles=<T extends {title:LocalText;excerpt:LocalText}>(base:T[])=>{const overrides=getArticleOverrides();return base.map((article,index)=>{const override=overrides.find(item=>item.index===index);return override?{...article,title:{...article.title,en:override.title},excerpt:{...article.excerpt,en:override.excerpt},demoStatus:override.status}:{...article,demoStatus:'Published' as const}})}

export const getSeoSettings=()=>read<SeoSettings>(KEYS.seo,defaultSeo)
export const saveSeoSettings=(value:SeoSettings)=>write(KEYS.seo,value)

export function resetDemoData(){localStorage.removeItem(KEYS.inquiries);localStorage.removeItem(KEYS.products);localStorage.removeItem(KEYS.articles);localStorage.removeItem(KEYS.seo);window.dispatchEvent(new Event('novamach-demo-updated'))}

export const localizedProductName=(slug:string,lang:Lang,base:Product[])=>{const product=getDemoProducts(base).find(item=>item.slug===slug);return product?product.name[lang]:slug||'General project inquiry'}
