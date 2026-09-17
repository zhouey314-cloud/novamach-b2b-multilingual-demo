from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sales-kit" / "01-end-customer" / "外贸独立站需求确认表-打印版.pdf"
FONT = "/System/Library/Fonts/STHeiti Light.ttc"
FONT_BOLD = "/System/Library/Fonts/STHeiti Medium.ttc"

pdfmetrics.registerFont(TTFont("NM-CN", FONT))
pdfmetrics.registerFont(TTFont("NM-CN-Bold", FONT_BOLD))

W, H = A4
INK = (0.09, 0.10, 0.09)
MUTED = (0.39, 0.42, 0.39)
LINE = (0.76, 0.78, 0.75)
ORANGE = (0.91, 0.34, 0.18)
PAPER = (0.965, 0.96, 0.94)


def set_fill(c, color):
    c.setFillColorRGB(*color)


def write(c, value, x, y, size=9, bold=False, color=INK):
    set_fill(c, color)
    c.setFont("NM-CN-Bold" if bold else "NM-CN", size)
    c.drawString(x, y, value)


def base_page(c, page, title, lead):
    set_fill(c, PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setStrokeColorRGB(*LINE)
    c.line(44, H - 50, W - 44, H - 50)
    write(c, "B2B WEBSITE / REQUIREMENT BRIEF", 44, H - 39, 7.5, True)
    write(c, f"客户填写版 · {page} / 03", W - 135, H - 39, 7.5, True, ORANGE)
    write(c, title, 44, H - 96, 24, True)
    write(c, lead, 44, H - 119, 8.5, False, MUTED)
    return H - 155


def section(c, title, y):
    set_fill(c, ORANGE)
    c.rect(44, y - 1, 3, 17, fill=1, stroke=0)
    write(c, title, 55, y + 2, 12, True)
    return y - 24


def field(c, label, x, y, width, height=42, hint=None):
    c.setStrokeColorRGB(*LINE)
    c.line(x, y - height, x + width, y - height)
    write(c, label, x, y - 10, 8.5, True)
    if hint:
        write(c, hint, x, y - 23, 6.8, False, MUTED)


def checkbox(c, label, x, y, width):
    c.setStrokeColorRGB(*MUTED)
    c.rect(x, y - 8, 8, 8, fill=0, stroke=1)
    write(c, label, x + 15, y - 8, 7.8)
    c.setStrokeColorRGB(*LINE)
    c.line(x, y - 19, x + width, y - 19)


def footer(c, left):
    c.setStrokeColorRGB(*LINE)
    c.line(44, 34, W - 44, 34)
    write(c, left, 44, 20, 6.4, False, MUTED)
    write(c, "Demonstration Website / Sample Data", W - 205, 20, 6.4, True, ORANGE)


def page_one(c):
    y = base_page(c, "01", "外贸独立站需求确认表", "用于第一次沟通前梳理公司、产品、市场与网站范围；尚未确认的项目可以填写“待确认”。")
    y = section(c, "基本信息", y)
    col = (W - 88 - 24) / 2
    rows = [
        ("公司名称", "行业 / 细分领域"),
        ("核心产品", "目标国家 / 市场"),
    ]
    for left, right in rows:
        field(c, left, 44, y, col)
        field(c, right, 44 + col + 24, y, col)
        y -= 50
    field(c, "当前网站及网址", 44, y, W - 88)
    y -= 50
    field(c, "喜欢的参考网站", 44, y, W - 88, 50, "请说明喜欢其视觉、结构、产品呈现或其他部分")
    y -= 58
    field(c, "主要联系人", 44, y, col)
    field(c, "最终决策人", 44 + col + 24, y, col)
    y -= 62
    y = section(c, "网站范围", y)
    checkbox(c, "展示站", 44, y, col)
    checkbox(c, "商城 / 电商", 44 + col + 24, y, col)
    y -= 28
    checkbox(c, "需要后台", 44, y, col)
    checkbox(c, "新闻 / 案例 / 下载中心", 44 + col + 24, y, col)
    y -= 38
    field(c, "预计页面数量", 44, y, col)
    field(c, "产品及分类数量", 44 + col + 24, y, col)
    y -= 50
    field(c, "语言及数量", 44, y, col)
    field(c, "后台人数与角色", 44 + col + 24, y, col)
    y -= 50
    field(c, "翻译来源", 44, y, W - 88, 42, "客户提供 / 机器翻译后人工审核 / 需要协助")
    footer(c, "自主 B2B 外贸独立站 Demo · 非真实客户案例")


def page_two(c):
    y = base_page(c, "02", "获客、系统与数据", "接口能力和业务流程会影响技术方案、周期与报价，请尽量填写已有账号、接口和数据情况。")
    col = (W - 88 - 24) / 2
    y = section(c, "获客与业务流程", y)
    field(c, "RFQ / Contact 询盘", 44, y, col)
    field(c, "WhatsApp 账号及使用方式", 44 + col + 24, y, col)
    y -= 50
    field(c, "Email 收件规则", 44, y, col)
    field(c, "SEO 需求", 44 + col + 24, y, col, hint="基础 / 持续运营 / 待确认")
    y -= 50
    field(c, "询盘后续流转", 44, y, W - 88, 46, "邮箱 / CRM / ERP / 人员分配 / 状态跟踪")
    y -= 62
    y = section(c, "系统与接口", y)
    labels = [
        ("CRM / ERP / 其他 API", "官方接口文档和测试环境已具备"),
        ("支付", "会员"),
        ("购物车 / 订单", "库存 / 税费 / 物流"),
    ]
    for left, right in labels:
        checkbox(c, left, 44, y, col)
        checkbox(c, right, 44 + col + 24, y, col)
        y -= 27
    field(c, "接口账号、权限与限制说明", 44, y, W - 88, 48)
    y -= 65
    y = section(c, "数据与基础设施", y)
    field(c, "是否迁移旧站数据", 44, y, col)
    field(c, "可提供的数据格式", 44 + col + 24, y, col)
    y -= 50
    field(c, "图片、文案、参数、证书由谁提供及审核", 44, y, W - 88)
    y -= 50
    field(c, "当前服务器 / 云服务", 44, y, col)
    field(c, "域名及管理权限", 44 + col + 24, y, col)
    y -= 50
    field(c, "部署地区或合规要求", 44, y, W - 88)
    footer(c, "本表用于需求澄清，不构成最终方案或报价")


def page_three(c):
    y = base_page(c, "03", "商务、时间与补充确认", "先确认需求、接口、账号权限和技术边界，再承诺方案、周期和报价。")
    col = (W - 88 - 24) / 2
    y = section(c, "商务与时间", y)
    field(c, "预算范围", 44, y, col)
    field(c, "希望上线时间", 44 + col + 24, y, col)
    y -= 50
    field(c, "期望的阶段验收方式", 44, y, W - 88)
    y -= 50
    field(c, "其他要求", 44, y, W - 88, 68)
    y -= 86
    y = section(c, "补充确认事项", y)
    questions = [
        "第三方系统是否提供官方 API、测试环境和必要权限？",
        "多语言内容由谁翻译、审核和持续维护？",
        "产品数据结构、数量、变体和迁移质量是否已确认？",
        "询盘需要进入邮箱、CRM、ERP，还是需要分配与状态流转？",
        "支付、电商、会员、库存和税费规则是否存在地区差异？",
        "域名、服务器、CDN、隐私、Cookie 与数据合规由谁负责？",
        "上线日期是否依赖内容、接口、账号或客户审批？",
    ]
    for index, question in enumerate(questions, 1):
        write(c, f"{index:02d}", 44, y, 7.5, True, ORANGE)
        write(c, question, 68, y, 8.2)
        c.setStrokeColorRGB(*LINE)
        c.line(68, y - 13, W - 44, y - 13)
        y -= 38
    field(c, "填写人", 44, y, col)
    field(c, "日期", 44 + col + 24, y, col)
    footer(c, "请将填写结果交给项目联系人继续评估")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(OUT), pagesize=A4, pageCompression=1)
    page_one(pdf)
    pdf.showPage()
    page_two(pdf)
    pdf.showPage()
    page_three(pdf)
    pdf.showPage()
    pdf.save()
    print(OUT)


if __name__ == "__main__":
    main()
