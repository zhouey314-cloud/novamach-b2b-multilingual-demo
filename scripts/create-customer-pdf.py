from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "NovaMach-外贸独立站客户能力介绍.pdf"
FONT = "/System/Library/Fonts/STHeiti Light.ttc"
FONT_BOLD = "/System/Library/Fonts/STHeiti Medium.ttc"

pdfmetrics.registerFont(TTFont("NM-CN", FONT))
pdfmetrics.registerFont(TTFont("NM-CN-Bold", FONT_BOLD))

W, H = landscape(A4)
INK = "#151815"
PAPER = "#F4F3EE"
ORANGE = "#EF5B28"
MUTED = "#70756F"
LINE = "#D4D6D0"


def color(hex_value):
    return tuple(int(hex_value[i:i+2], 16) / 255 for i in (1, 3, 5))


def text(c, value, x, y, size=10, bold=False, fill=INK):
    c.setFillColorRGB(*color(fill))
    c.setFont("NM-CN-Bold" if bold else "NM-CN", size)
    c.drawString(x, y, value)


def lines(c, values, x, y, size, leading, bold=False, fill=INK):
    for index, value in enumerate(values):
        text(c, value, x, y - index * leading, size, bold, fill)


def footer(c, dark=False):
    line_color = "#343834" if dark else LINE
    c.setStrokeColorRGB(*color(line_color))
    c.line(38, 31, W - 38, 31)
    text(c, "自主 B2B 外贸独立站 Demo · 非真实客户案例", 38, 17, 6.6, False, "#929791" if dark else MUTED)
    text(c, "Demonstration Website / Sample Data", W - 190, 17, 6.6, True, ORANGE)


def top(c, left, page, dark=False):
    line_color = "#343834" if dark else LINE
    c.setStrokeColorRGB(*color(line_color))
    c.line(38, H - 42, W - 38, H - 42)
    text(c, left, 38, H - 30, 7.5, True, "#FFFFFF" if dark else INK)
    text(c, f"客户介绍版 · {page} / 03", W - 130, H - 30, 7, False, ORANGE)


def draw_cover_image(c, path, x, y, width, height):
    image = Image.open(path)
    src_ratio = image.width / image.height
    dst_ratio = width / height
    if src_ratio > dst_ratio:
        crop_width = int(image.height * dst_ratio)
        left = (image.width - crop_width) // 2
        image = image.crop((left, 0, left + crop_width, image.height))
    else:
        crop_height = int(image.width / dst_ratio)
        top_crop = 0
        image = image.crop((0, top_crop, image.width, min(image.height, top_crop + crop_height)))
    c.drawImage(ImageReader(image), x, y, width, height, preserveAspectRatio=False, mask="auto")


def draw_contain_image(c, path, x, y, width, height, background="#222522"):
    """Place the complete screenshot inside the frame without cropping its edges."""
    image = Image.open(path)
    scale = min(width / image.width, height / image.height)
    draw_width = image.width * scale
    draw_height = image.height * scale
    draw_x = x + (width - draw_width) / 2
    draw_y = y + (height - draw_height) / 2
    c.setFillColorRGB(*color(background))
    c.rect(x, y, width, height, fill=1, stroke=0)
    c.drawImage(ImageReader(image), draw_x, draw_y, draw_width, draw_height, preserveAspectRatio=True, mask="auto")


def page_one(c):
    c.setFillColorRGB(*color(INK)); c.rect(0, 0, W, H, fill=1, stroke=0)
    top(c, "NOVAMACH / SALES DEMO", "01", True)
    text(c, "工业 B2B 外贸独立站", 46, H - 92, 8, True, ORANGE)
    lines(c, ["让产品能力", "成为海外客户", "看得懂的答案。"], 46, H - 136, 35, 39, True, "#FFFFFF")
    lines(c, ["自主 B2B 外贸独立站 Demo · 非真实客户案例", "本演示用于展示页面、产品、多语言、询盘与内容维护能力。"], 47, H - 275, 9.5, 16, False, "#B9BDB7")
    image_path = ROOT / "outputs" / "sales-screenshots" / "01-首页-桌面.png"
    draw_contain_image(c, image_path, 475, 128, 325, 300)
    c.setFillColorRGB(*color(ORANGE)); c.rect(455, 115, 12, 325, fill=1, stroke=0)
    items = ["高级品牌首页", "产品分类与详情", "English / 简体中文 / Español", "Desktop / Tablet / Mobile", "RFQ 询盘路径", "演示内容后台"]
    for i, item in enumerate(items):
        x = 47 + (i % 3) * 130
        y = 92 - (i // 3) * 32
        text(c, f"{i+1:02d}", x, y, 7, True, ORANGE)
        text(c, item, x + 20, y, 7.5, False, "#FFFFFF")
    footer(c, True)


def page_two(c):
    c.setFillColorRGB(*color(PAPER)); c.rect(0, 0, W, H, fill=1, stroke=0)
    top(c, "关键 Demo 画面", "02")
    text(c, "从第一印象到询盘入口", 42, H - 78, 7.5, True, ORANGE)
    text(c, "清晰呈现，层层推进。", 42, H - 113, 27, True)
    text(c, "访客从品牌首页进入产品详情，理解特点与参数，再提交结构化询盘；后台仅演示内容与线索维护。", 42, H - 137, 8, False, MUTED)
    home = ROOT / "outputs" / "sales-screenshots" / "01-首页-桌面.png"
    product = ROOT / "outputs" / "sales-screenshots" / "03-产品详情.png"
    admin = ROOT / "outputs" / "sales-screenshots" / "06-后台Dashboard.png"
    draw_cover_image(c, home, 42, 80, 390, 285)
    draw_cover_image(c, product, 450, 238, 350, 127)
    draw_cover_image(c, admin, 450, 80, 350, 127)
    c.setFillColorRGB(*color("#FFFFFF")); c.rect(42, 63, 390, 22, fill=1, stroke=0)
    c.rect(450, 221, 350, 22, fill=1, stroke=0); c.rect(450, 63, 350, 22, fill=1, stroke=0)
    text(c, "01 / HOME  品牌定位、产品矩阵、行业方案与行动入口", 51, 70, 6.5, False, MUTED)
    text(c, "02 / PRODUCT  产品特点、参数与应用场景", 459, 228, 6.5, False, MUTED)
    text(c, "03 / ADMIN DEMO  模拟内容与询盘工作流", 459, 70, 6.5, False, MUTED)
    footer(c)


def page_three(c):
    c.setFillColorRGB(*color(PAPER)); c.rect(0, 0, W, H, fill=1, stroke=0)
    top(c, "标准合作流程", "03")
    text(c, "先把范围说清楚，再把项目做好", 42, H - 78, 7.5, True, ORANGE)
    text(c, "四步完成一套可验收的网站。", 42, H - 113, 27, True)
    text(c, "正式项目以客户确认的真实资料为准；接口、内容量、语言数量与上线条件会在报价前确认。", 42, H - 137, 8, False, MUTED)
    process = [
        ("01", "需求确认", ["确认品牌、产品、市场、语言、", "页面、资料与上线目标。"]),
        ("02", "内容与设计", ["梳理信息结构，确定视觉方向，", "完成核心页面与内容表达。"]),
        ("03", "开发与验收", ["响应式开发、内容配置、表单与", "导航检查，按清单验收。"]),
        ("04", "上线与支持", ["配置域名与托管，交付使用说明；", "扩展项另行确认。"]),
    ]
    for i, (number, title, desc) in enumerate(process):
        x = 42 + (i % 2) * 390
        y = 282 - (i // 2) * 132
        c.setStrokeColorRGB(*color(LINE)); c.rect(x, y, 370, 112, fill=0, stroke=1)
        text(c, number, x + 18, y + 73, 20, True, "#BEC1BA")
        text(c, title, x + 75, y + 75, 16, True)
        lines(c, desc, x + 75, y + 48, 7.5, 12, False, MUTED)
    c.setFillColorRGB(*color(ORANGE)); c.rect(42, 47, 760, 57, fill=1, stroke=0)
    text(c, "建议下一步", 58, 82, 6.5, False, "#FFFFFF")
    text(c, "提供公司、产品、目标市场、语言与参考网站，我们据此确认页面、周期与预算。", 58, 61, 9.5, True, "#FFFFFF")
    footer(c)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(OUT), pagesize=landscape(A4), pageCompression=1)
    page_one(pdf); pdf.showPage()
    page_two(pdf); pdf.showPage()
    page_three(pdf); pdf.showPage()
    pdf.save()
    print(OUT)


if __name__ == "__main__":
    main()
