"""
Generate Yuanyuan Xu's Academic CV PDF (Chinese) — elegant sans-serif edition.
Uses 微软雅黑 (Microsoft YaHei) for elegant sans-serif Chinese typography.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable
)
from reportlab.lib.colors import black, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "YuanyuanXu_CV_CN.pdf")

FONT_DIR = "C:/Windows/Fonts"

def try_register(name, filenames, subfont=0):
    for fn in filenames:
        p = os.path.join(FONT_DIR, fn)
        if os.path.exists(p):
            try:
                pdfmetrics.registerFont(TTFont(name, p, subfontIndex=subfont))
                print(f"  Registered {name} from {fn}")
                return True
            except Exception as e:
                print(f"  Failed {fn}: {e}")
    return False

# Microsoft YaHei (微软雅黑) - elegant sans-serif
ok_r = try_register('YHRegular', ['msyh.ttc', 'msyh.ttf', 'MicrosoftYaHei.ttf'], subfont=0)
ok_b = try_register('YHBold', ['msyhbd.ttc', 'msyhbd.ttf', 'MicrosoftYaHeiBold.ttf'], subfont=0)

if not ok_r:
    # Fallback to SimHei (sans-serif Chinese)
    try_register('YHRegular', ['simhei.ttf', 'SimHei.ttf'])
    try_register('YHBold', ['simhei.ttf', 'SimHei.ttf'])

if not ok_b:
    ok_b = try_register('YHBold', ['msyh.ttc', 'msyh.ttf', 'simhei.ttf', 'SimHei.ttf'], subfont=0)

# Also register Calibri for Latin text
try_register('CalibriR', ['calibri.ttf', 'Calibri.ttf'])
try_register('CalibriB', ['calibrib.ttf'])
try_register('CalibriI', ['calibrii.ttf'])

FONT_R = 'YHRegular'
FONT_B = 'YHBold'

MARGIN = 0.85 * inch
PAGE_W, PAGE_H = letter

DARK = HexColor('#1a1a2e')
ACCENT = HexColor('#2D5A3D')
RULE_COLOR = HexColor('#999999')

styles = {
    'name': ParagraphStyle('Name', fontName=FONT_B, fontSize=18, alignment=TA_CENTER, spaceAfter=2, textColor=DARK, leading=24),
    'en_name': ParagraphStyle('EnName', fontName='CalibriR', fontSize=10, alignment=TA_CENTER, spaceAfter=6, textColor=HexColor('#666666')),
    'contact': ParagraphStyle('Contact', fontName=FONT_R, fontSize=9.5, alignment=TA_CENTER, leading=14, spaceAfter=4, textColor=HexColor('#444444')),
    'section': ParagraphStyle('Section', fontName=FONT_B, fontSize=11, alignment=TA_LEFT, spaceBefore=14, spaceAfter=6, textColor=DARK, leading=14),
    'subsection': ParagraphStyle('Subsection', fontName=FONT_B, fontSize=9.5, alignment=TA_LEFT, spaceBefore=8, spaceAfter=3, textColor=HexColor('#333333')),
    'entry_title': ParagraphStyle('EntryTitle', fontName=FONT_B, fontSize=9.5, leading=13, textColor=DARK),
    'entry_body': ParagraphStyle('EntryBody', fontName=FONT_R, fontSize=9.5, leading=13, textColor=HexColor('#333333')),
    'entry_italic': ParagraphStyle('EntryItalic', fontName=FONT_R, fontSize=9.5, leading=13, textColor=HexColor('#555555')),
    'date': ParagraphStyle('Date', fontName=FONT_R, fontSize=9, leading=13, textColor=HexColor('#666666')),
}

DATE_COL = 1.1 * inch
DETAIL_COL = PAGE_W - 2*MARGIN - DATE_COL - 0.1*inch

def build_cv():
    doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=0.7*inch, bottomMargin=0.7*inch)

    story = []

    # ---- HEADER ----
    story.append(Paragraph("\u5f90\u56ed\u56ed", styles['name']))
    story.append(Paragraph("Yuanyuan Xu", styles['en_name']))
    story.append(HRFlowable(width="100%", thickness=0.8, color=RULE_COLOR, spaceAfter=6))
    story.append(Paragraph(
        "\u535a\u58eb\u7814\u7a76\u751f\uff0c\u8de8\u5b66\u79d1\u7814\u7a76<br/>"
        "\u521b\u610f\u4e0e\u6279\u5224\u7814\u7a76\u5b66\u9662\uff0c\u4e0d\u5217\u98a0\u54e5\u4f26\u6bd4\u4e9a\u5927\u5b66 (UBC)",
        styles['contact']))
    story.append(HRFlowable(width="100%", thickness=0.4, color=RULE_COLOR, spaceBefore=2, spaceAfter=8))

    B = FONT_B
    R = FONT_R

    def section(title):
        story.append(HRFlowable(width="100%", thickness=0.3, color=HexColor('#cccccc'), spaceBefore=4, spaceAfter=0))
        story.append(Paragraph(title, styles['section']))

    def subsec(title):
        story.append(Paragraph(title, styles['subsection']))

    def entry(date, lines, sp=4):
        date_p = Paragraph(date, styles['date'])
        if len(lines) == 1:
            t = Table([[date_p, lines[0]]], colWidths=[DATE_COL, DETAIL_COL])
        else:
            inner = [[l] for l in lines]
            inner_t = Table(inner, colWidths=[DETAIL_COL])
            inner_t.setStyle(TableStyle([
                ('VALIGN',(0,0),(-1,-1),'TOP'),
                ('TOPPADDING',(0,0),(-1,-1),0),
                ('BOTTOMPADDING',(0,0),(-1,-1),1),
                ('LEFTPADDING',(0,0),(-1,-1),0),
                ('RIGHTPADDING',(0,0),(-1,-1),0),
            ]))
            t = Table([[date_p, inner_t]], colWidths=[DATE_COL, DETAIL_COL])
        t.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('TOPPADDING',(0,0),(-1,-1),1),
            ('BOTTOMPADDING',(0,0),(-1,-1),sp),
            ('LEFTPADDING',(0,0),(-1,-1),0),
            ('RIGHTPADDING',(0,0),(-1,-1),0),
        ]))
        story.append(t)

    def P(text, style='entry_body'):
        return Paragraph(text, styles[style])

    def pub(authors, title, venue, doi=None):
        t = f'{authors}. <font name="{B}">\u300c{title}\u300d</font> {venue}'
        if doi: t += f' <font color="#2D5A3D">{doi}</font>'
        return P(t)

    # ---- \u6559\u80b2\u80cc\u666f ----
    section("\u6559\u80b2\u80cc\u666f")
    entry("2025 \u2013 2029", [
        P(f'<font name="{B}">\u8de8\u5b66\u79d1\u7814\u7a76\u535a\u58eb (Ph.D.)</font>','entry_title'),
        P(f'\u4e0d\u5217\u98a0\u54e5\u4f26\u6bd4\u4e9a\u5927\u5b66 (University of British Columbia)'),
        P(f'创意与批判研究学院。导师：Prof. Aleksandra Dulic（教授，FCCS）和 Prof. Patricia Lasserre（副教授，计算机科学）。研究方向：与原住民社区共同设计教育游戏以促进环境韧性。全额资助：OGRS (CAD $25,000/年) 及 IDPT 学费减免。')
    ])
    entry("2020 \u2013 2023", [
        P(f'<font name="{B}">工学硕士 (M.Eng.)</font>','entry_title'),
        P('同济大学设计创意学院，上海'),
        P('全额奖学金 (¥32,000)。毕业典礼代表发言 (2023)。')
    ])
    entry("2016 \u2013 2020", [
        P(f'<font name="{B}">文学学士 (B.A.)</font>','entry_title'),
        P('华东理工大学，上海'),
        P('GPA: 3.7/4.0，连续四年专业排名第一。国家奖学金 (前0.2%, ¥8,000)。成思危名誉校长奖学金 (前1%)。特等学业奖学金 (连续5学期)。年度人物提名。「榜样力量」代言人。上海市优秀毕业生 (前2%)。毕业典礼代表发言 (2020)。')
    ])
    entry("2023 \u2013 2025", [
        P(f'<font name="{B}">游戏设计、动画与视觉特效文凭</font>','entry_title'),
        P('Think Tank Training Centre\uff0c\u6e29\u54e5\u534e'),
        P('\u5168\u6d41\u7a0b\u6e38\u620f\u5236\u4f5c\uff1a3D\u52a8\u753b\u3001\u89c6\u89c9\u7279\u6548\u3001\u6e38\u620f\u8bbe\u8ba1\u3002')
    ])

    # ---- \u7814\u7a76\u5c97\u4f4d ----
    section("\u7814\u7a76\u5c97\u4f4d")
    entry("2025\u5e749\u6708 \u2013 \u81f3\u4eca", [
        P(f'<font name="{B}">\u7814\u7a76\u52a9\u7406 \u2014 \u6587\u5316\u4e0e\u6280\u672f\u4e2d\u5fc3</font>','entry_title'),
        P('\u4e0d\u5217\u98a0\u54e5\u4f26\u6bd4\u4e9a\u5927\u5b66'),
        P('Beaver Worlds\u9879\u76ee\uff1a\u53c2\u4e0e\u5f0f\u6e38\u620f\u8bbe\u8ba1\uff0c\u7528\u4e8eOkanagan\u6c34\u8d44\u6e90\u6cbb\u7406\u4e0e\u539f\u4f4f\u6c11\u77e5\u8bc6\u4f20\u64ad\u3002')
    ])

    # ---- \u8bba\u6587\u53d1\u8868 ----
    section("\u8bba\u6587\u53d1\u8868")

    subsec("\u671f\u520a\u8bba\u6587")
    for a,t,v,d in [
        ("<b>Y. Xu</b>, Z. Sun, C. Zhen, Y.-S. Lin, T.H. Sarker, M. Thorogood, P. Lasserre, A. Dulic","\u4ece\u53c2\u4e0e\u5230\u97e7\u6027\uff1a\u57fa\u4e8e\u6e38\u620f\u7684\u73af\u5883\u97e7\u6027\u5b66\u4e60\u7cfb\u7edf\u7efc\u8ff0","Sustainability, 18(5), 2305, 2026","doi.org/10.3390/su18052305"),
        ("<b>Y. Xu*</b>, X. Shan, M. Guo, W. Gao, Y.-S. Lin","\u5ba2\u6237\u611f\u77e5\u4ef7\u503c\u89c6\u89d2\u4e0b\u7684\u4f53\u9a8c\u7ba1\u7406\u5de5\u5177\u8bbe\u8ba1\u4e0e\u5e94\u7528","World Electric Vehicle Journal, 15(8), 378, 2024","doi.org/10.3390/wevj15080378"),
        ("<b>Y. Xu*</b>, W. Gao, Y. Wang, X. Shan, Y.-S. Lin","\u589e\u5f3a\u9ad8\u7ea7LLM\u5bf9\u8bdd\u4ee3\u7406\u7684\u7528\u6237\u4f53\u9a8c\u4e0e\u4fe1\u4efb","Computing and Artificial Intelligence, 2(2), 1467, 2024","doi.org/10.59400/cai.v2i2.1467"),
        ("<b>Y. Xu*</b>, Y.-S. Lin, X. Zhou, X. Shan","\u5229\u7528\u60c5\u611f\u8bc6\u522b\u6280\u672f\u5b9e\u65f6\u63d0\u5347\u7528\u6237\u4f53\u9a8c","Computing and Artificial Intelligence, 2(1), 1388, 2024","doi.org/10.59400/cai.v2i1.1388"),
        ("M. Liu*, M. Guo, L. Jiang, <b>Y. Xu</b>","\u57fa\u4e8e\u611f\u6027\u5de5\u5b66\u7684\u4ea7\u54c1\u9020\u578b\u8bbe\u8ba1\uff1a\u996e\u5177\u7684\u773c\u52a8\u8ffd\u8e2a\u7814\u7a76","\u4e0a\u6d77\u7406\u5de5\u5927\u5b66\u5b66\u62a5, 42(5), 2020","doi.org/10.13255/j.cnki.jusst.20191122008"),
        ("<b>Y. Xu*</b>, Y. Bao, B. Yang","\u81ea\u95ed\u75c7\u513f\u7ae5\u6cbb\u7597\u73a9\u5177\u8bbe\u8ba1\u5206\u6790","\u827a\u672f\u79d1\u6280, 2018",None),
        ("M. Liu*, M. Guo, L. Jiang, <b>Y. Xu</b>","\u773c\u52a8\u8ffd\u8e2a\u6570\u636e\u4e0e\u4ea7\u54c1\u9020\u578b\u8bbe\u8ba1\u5173\u7cfb\u63a2\u7a76","\u6587\u5b66\u751f\u6d3b, 2019","doi.org/10.3969/j.issn.1005-5312.2019.10.029"),
    ]: entry("", [pub(a,t,v,d)], sp=3)

    subsec("\u4f1a\u8bae\u8bba\u6587\u4e0e\u4e66\u7ae0\u8282")
    for a,t,v,d in [
        ("<b>Y. Xu*</b>, X. Shan, Y.-S. Lin, J. Wang","\u8de8\u6587\u5316\u6e38\u620f\u8bbe\u8ba1\u7684AI\u589e\u5f3a\u5de5\u5177","HCII 2024, LNCS 15377, Springer, 2025","doi.org/10.1007/978-3-031-76812-5_29"),
        ("X. Shan, <b>Y. Xu*</b>, Y. Wang, Y.-S. Lin, Y. Bao","\u5927\u8bed\u8a00\u6a21\u578b\u7684\u8de8\u6587\u5316\u542b\u4e49","HCII 2024, LNCS 15375, Springer, 2025","doi.org/10.1007/978-3-031-76806-4_8"),
        ("T. Xia*, <b>Y. Xu</b>, X. Shan","KOA-Monitor: \u6570\u5b57\u5e72\u9884\u4e0e\u529f\u80fd\u8bc4\u4f30\u7cfb\u7edf","HCII 2025, LNCS 15810, Springer, 2025","doi.org/10.1007/978-3-031-92710-2_26"),
        ("X. Shan, <b>Y. Xu*</b>, T. Xia, Y.-S. Lin","\u4e3a\u6240\u6709\u4eba\u8bbe\u8ba1\u8461\u8404\u9152\u54c1\u5c1d\u4f53\u9a8c","HCII 2025, Springer, 2025",None),
        ("X. Shan, <b>Y. Xu</b>, T. Xia, Y.-S. Lin","\u91cd\u65b0\u601d\u8003\u4e2d\u56fd\u6d88\u8d39\u8005\u7684\u8461\u8404\u9152\u54c1\u5c1d","2025 IEEE International Conference on Content-Based Multimedia Indexing (CBMI), 2025",None),
        ("<b>Y. Xu*</b>, Y.-S. Lin","\u7528\u6237\u611f\u77e5\u4ef7\u503c\u5bf9\u65b0\u80fd\u6e90\u6c7d\u8f66\u4f01\u4e1a\u7684\u5f71\u54cd\u63a2\u7a76","FFIT 2024, Atlantis Press, 2024","doi.org/10.2991/978-94-6463-572-0_2"),
        ("G. Tian, <b>Y. Xu*</b>","\u4eff\u897f\u590f\u6587\u6c49\u5b57\u5b57\u4f53\u8bbe\u8ba1\u65b9\u6cd5\u7814\u7a76","AEHSSR, 2022","doi.org/10.56028/aehssr.2.1.270"),
    ]: entry("", [pub(a,t,v,d)], sp=3)

    subsec("\u5373\u5c06\u53d1\u8868\uff08\u5f55\u7528\uff09")
    for a,t,v in [
        ("<b>Y. Xu</b> et al.","\u751f\u6001\u5171\u60c5\u6620\u5c04\uff1a3D\u73af\u5883\u6559\u80b2\u6e38\u620f\u4e2d\u73a9\u5bb6\u611f\u77e5\u7684\u8bed\u4e49\u7f51\u7edc\u5206\u6790","HCII 2026, LNCS, Springer"),
        ("C. Zhen, <b>Y. Xu</b> et al.","\u52a8\u753b\u8bbe\u8ba1\u54f2\u5b66\u5728 3D \u6559\u80b2\u6e38\u620f\u4e2d\u7684\u5e94\u7528\uff1aBeaver Worlds\u7684\u5f00\u53d1","HCII 2026, CCIS, Springer"),
        ("Z. Sun, <b>Y. Xu</b> et al.","\u6311\u6218\u5373\u5fc3\u6d41\uff1a\u9b42\u7c7b\u6e38\u620f\u7684\u8bbe\u8ba1\u4e0e\u4f53\u9a8c","HCII 2026, LNCS, Springer"),
        ("<b>Y. Xu</b> et al.","\u751f\u6001\u6e38\u620f\u4e2d\u7f3a\u5e2d\u7684\u6559\u5e08\uff1a\u6559\u5e08\u6574\u5408\u7684\u7406\u8bba\u6846\u67b6","DiGRA 2026"),
        ("<b>Y. Xu</b>, P. Lasserre, A. Dulic","\u4ece\u8d44\u6e90\u5230\u4eb2\u5c5e\uff1aOkanagan\u5730\u533a\u73af\u5883\u97e7\u6027\u8bbe\u8ba1","DiGRA 2026"),
        ("Z. Sun, <b>Y. Xu</b> et al.","\u91cd\u65b0\u5ba1\u89c6VR\u6e38\u620f\u8bbe\u8ba1\u4e2d\u7684\u8d85\u5199\u5b9e\u8ffd\u6c42","DiGRA 2026"),
    ]: entry("", [pub(a,t,v)], sp=3)

    subsec("\u4e13\u5229")
    entry("2023", [P(f'X. Sun \u7b49, <font name="{B}">Y. Xu</font>. <font name="{B}">\u300cFPGA\u89c6\u89c9\u76f2\u4eba\u5bfc\u822a\u65b9\u6cd5\u300d</font> (CN110070514B). \u4e2d\u56fd\u4e13\u5229\u5c40\u3002\u5df2\u6388\u6743\u3002')])

    # ---- \u5b66\u672f\u62a5\u544a ----
    section("\u5b66\u672f\u62a5\u544a\u4e0e\u53d1\u8868")
    entry("2026年6月", [P(f'<font name="{B}">Y. Xu</font> 等。三篇论文。国际人机交互大会 (HCII) 2026，蒙特利尔。')])
    entry("2026年6月", [P(f'<font name="{B}">Y. Xu</font> 等。博士生研讨会及教育专题。数字游戏研究协会年会 (DiGRA) 2026，爱尔兰。')])
    entry("2025", [P(f'<font name="{B}">Y. Xu</font>, Y.-S. Lin. 「Situated Bodies, Wandering Minds」 ACM 计算机图形与交互技术会议 (SIGGRAPH) 2025，温哥华 — BOF 专场。')])
    entry("2024", [P(f'<font name="{B}">Y. Xu</font>. 「Creativity for Sensational Perception」 国际人机交互大会 (HCII) 2024，华盛顿 DC。')])
    entry("2023", [P(f'<font name="{B}">Y. Xu</font>. 毕业典礼代表发言。同济大学。')])
    entry("2020", [P(f'<font name="{B}">Y. Xu</font>. 毕业典礼代表发言。华东理工大学。')])

    # ---- \u7814\u7a76\u8d44\u52a9 ----
    section("\u7814\u7a76\u8d44\u52a9\u4e0e\u5956\u5b66\u91d1")
    entry("2025", [
        P(f'<font name="{B}">Okanagan\u7814\u7a76\u751f\u5956\u5b66\u91d1 (OGRS) + \u56fd\u9645\u535a\u58eb\u90e8\u5206\u5b66\u8d39\u51cf\u514d (IDPT)</font>','entry_title'),
        P('\u4e0d\u5217\u98a0\u54e5\u4f26\u6bd4\u4e9a\u5927\u5b66\u30024\u5e74\u535a\u58eb\u8d44\u52a9\u3002')
    ])
    entry("2022", [
        P(f'<font name="{B}">\u4e0a\u6d77\u79d1\u6280\u521b\u4e1a\u57fa\u91d1\u4f1a (EFG) \u2014 50\u4e07\u5143</font>','entry_title'),
        P('\u8d1f\u8d23\u4eba\u3002\u300c\u8bbe\u8ba1\u7ae5\u5e74\uff1a\u6e38\u620f\u3001\u60c5\u611f\u4e0e\u6bdb\u7ed2\u73a9\u5177\u300d\u3002')
    ])
    entry("2017", [P(f'<font name="{B}">\u4e0a\u6d77\u9ad8\u6821\u4e00\u6d41\u5b66\u79d1\u5efa\u8bbe\u57fa\u91d1</font>','entry_title'), P('\u5b66\u751f\u7814\u7a76\u5458\u3002\u300c\u57fa\u4e8e\u611f\u6027\u5de5\u5b66\u7684\u7528\u6237\u611f\u77e5\u5206\u6790\u300d\u3002')])
    entry("2017", [P(f'<font name="{B}">\u56fd\u5bb6\u81ea\u7136\u79d1\u5b66\u57fa\u91d1 (No. 51905175)</font>','entry_title'), P('\u5b66\u751f\u7814\u7a76\u5458\u3002\u300c\u611f\u6027\u5de5\u5b66\u4ea7\u54c1\u9020\u578b\u8bbe\u8ba1\u300d\u3002')])
    entry("2017", [P(f'<font name="{B}">\u4e0a\u6d77\u5927\u5b66\u751f\u521b\u65b0\u521b\u4e1a\u8bad\u7ec3\u9879\u76ee (No. X18223)</font>','entry_title'), P('\u9879\u76ee\u8d1f\u8d23\u4eba\u3002')])

    # ---- \u6559\u5b66\u7ecf\u5386 ----
    section("\u6559\u5b66\u7ecf\u5386")
    entry("2026\u5e741\u6708 \u2013 \u81f3\u4eca", [
        P(f'<font name="{B}">\u52a9\u6559 \u2014 CCS 325: \u4eba\u5de5\u667a\u80fd\u4e0e\u521b\u610f</font>','entry_title'),
        P('\u4e0d\u5217\u98a0\u54e5\u4f26\u6bd4\u4e9a\u5927\u5b66'),
        P('\u8bc4\u5206\u3001\u8f85\u5bfc\u8bfe\u3001\u5b66\u751f\u53cd\u9988\uff0c\u5f15\u5bfc\u751f\u6210\u5f0fAI\u4e0e\u521b\u610f\u7f16\u7a0b\u6d3b\u52a8\u3002')
    ])
    entry("2025\u5e7412\u6708 \u2013 2026\u5e742\u6708", [
        P(f'<font name="{B}">\u8bc4\u5206\u5458 (Marker) \u2014 CCS 330\uff1a\u6e38\u620f\u8bbe\u8ba1</font>','entry_title'),
        P('\u4e0d\u5217\u98a0\u54e5\u4f26\u6bd4\u4e9a\u5927\u5b66'),
        P('\u8d1f\u8d23\u6e38\u620f\u8bbe\u8ba1\u8bfe\u7a0b\u7684\u4f5c\u4e1a\u8bc4\u5206\u4e0e\u4e66\u9762\u53cd\u9988\u3002')
    ])
    entry("2018 \u2013 2020", [
        P(f'<font name="{B}">\u52a9\u6559 \u2014 \u8bbe\u8ba1\u56fe\u5b66\uff08\u4e0a\u6d77\u5e02\u7cbe\u54c1\u8bfe\u7a0b\uff09</font>','entry_title'),
        P('\u534e\u4e1c\u7406\u5de5\u5927\u5b66'),
        P('\u5de5\u7a0b\u5236\u56fe\u3001\u6570\u5b57\u63d2\u753b\u4e0e\u8bbe\u8ba1\u57fa\u7840\u3002')
    ])

    # ---- \u884c\u4e1a\u7ecf\u5386 ----
    section("\u884c\u4e1a\u7ecf\u5386")
    entry("2022 \u2013 2023", [P(f'<font name="{B}">\u4ea7\u54c1\u7ecf\u7406</font> \u2014 SAP Labs\uff0cSAP Analytics Cloud\uff0c\u4e0a\u6d77','entry_title'), P('\u7528\u6237\u4f53\u9a8c\u4e0e\u5206\u6790\u9879\u76ee\u4e3b\u5bfc\uff1b\u4e3a\u4f01\u4e1a\u7528\u6237\u7ec4\u7ec7\u7814\u8ba8\u4f1a\uff1b\u6f14\u793a\u4e0e\u7528\u6237\u6d4b\u8bd5\u3002')])
    entry("2020", [P(f'<font name="{B}">\u4ea7\u54c1\u7ecf\u7406\u5b9e\u4e60\u751f</font> \u2014 \u897f\u95e8\u5b50\uff0c\u667a\u80fd\u57fa\u7840\u8bbe\u65bd\uff0c\u4e0a\u6d77','entry_title'), P('\u897f\u95e8\u5b508PT\u914d\u7535\u67dc\u5ba2\u6237\u57f9\u8bad\u4e0e\u9500\u552e\u652f\u6301\u3002')])
    entry("2020", [P(f'<font name="{B}">UX\u8bbe\u8ba1\u5e08\u5b9e\u4e60\u751f</font> \u2014 \u4e0a\u6d77\u5bb6\u5316\uff0c\u6d88\u8d39\u54c1\uff0c\u4e0a\u6d77','entry_title'), P('\u7528\u6237\u7814\u7a76\u4e0e\u6d88\u8d39\u54c1\u6570\u5b57\u5e73\u53f0\u7528\u6237\u4f53\u9a8c\u8bbe\u8ba1\u3002')])
    entry("2017 \u2013 2019", [P(f'<font name="{B}">\u8054\u5408\u521b\u59cb\u4eba</font> \u2014 \u4eab\u73a9 SharePlay\uff0c\u4e0a\u6d77','entry_title'), P('\u5a31\u4e50\u8bbe\u5907\u5171\u4eab\u5e73\u53f0\u3002\u521b\u9752\u6625\u5168\u56fd\u91d1\u5956\u3002')])

    # ---- \u5b66\u672f\u670d\u52a1 ----
    section("\u5b66\u672f\u670d\u52a1")
    story.append(P(
        f'<font name="{B}">ACM 人因与计算系统会议 (CHI)</font> \u2014 杰出审稿人特别认可，两次 (2025)<br/>'
        f'<font name="{B}">ACM 交互系统设计会议 (DIS)</font> &nbsp;&nbsp; <font name="{B}">ACM 创造力与认知会议 (C&amp;C)</font><br/>'
        f'<font name="{B}">ACM 用户界面软件与技术研讨会 (UIST)</font> &nbsp;&nbsp; <font name="{B}">ACM 眼动追踪研究与应用研讨会 (ETRA)</font><br/>'
        f'<font name="{B}">ACM 交互媒体体验国际会议 (IMX)</font> &nbsp;&nbsp; <font name="{B}">ACM 对话用户界面会议 (CUI)</font><br/>'
        f'<font name="{B}">ACM 汽车用户界面与交互式车载应用会议 (AutoUI)</font><br/>'
        f'<font name="{B}">IEEE 混合与增强现实国际研讨会 (ISMAR)</font> &nbsp;&nbsp; <font name="{B}">IEEE 虚拟现实与3D用户界面会议 (IEEE VR)</font><br/>'
        f'<font name="{B}">Eurographics/IEEE 可视化会议 (EuroVis)</font><br/>'
        f'<font name="{B}">亚洲计算机辅助建筑设计研究协会 (CAADRIA)</font> \u2014 国际审委会委员<br/>'
        f'<font name="{B}">国际人机交互期刊 (IJHCI)</font> &nbsp;&nbsp; <font name="{B}">创新技术进展 (ITA)</font>'
    ))
    story.append(Spacer(1, 8))

    # ---- \u83b7\u5956\u4e0e\u8363\u8a89 ----
    section("\u83b7\u5956\u4e0e\u8363\u8a89")
    for y, d in [
        ("2025","Okanagan\u7814\u7a76\u751f\u5956\u5b66\u91d1 (OGRS) \u2014 \u4e0d\u5217\u98a0\u54e5\u4f26\u6bd4\u4e9a\u5927\u5b66\uff0cCAD $25,000/\u5e74\uff0c4\u5e74\u535a\u58eb\u8d44\u52a9"),
        ("2025","\u56fd\u9645\u535a\u58eb\u90e8\u5206\u5b66\u8d39\u51cf\u514d (IDPT) \u2014 \u4e0d\u5217\u98a0\u54e5\u4f26\u6bd4\u4e9a\u5927\u5b66"),
        ("2025","杰出审稿人特别认可，两次 \u2014 ACM 人因与计算系统会议 (CHI)"),
        ("2025","Rookie of the Year \u2014 A Ranking (\u6e38\u620f\u7c7b) \u2014 The Rookies Awards"),
        ("2024","Rookie of the Year \u2014 A Ranking (视觉特效及3D动画) \u2014 The Rookies Awards"),
        ("2023","\u6bd5\u4e1a\u5178\u793c\u4ee3\u8868\u53d1\u8a00 \u2014 \u540c\u6d4e\u5927\u5b66"),
        ("2021","\u5168\u989d\u5956\u5b66\u91d1 (\u00a532,000) \u2014 \u540c\u6d4e\u5927\u5b66"),
        ("2021","\u94dc\u5956 \u2014 \u56fd\u9645\u6d77\u6d0b\u827a\u672f\u8282 (IOAF) \u6d77\u661f\u56fd\u9645\u9752\u5e74\u827a\u672f\u5bb6\u5c55"),
        ("2020","\u4e0a\u6d77\u5e02\u4f18\u79c0\u6bd5\u4e1a\u751f (\u524d2%) \u2014 \u4e0a\u6d77\u5e02\u6559\u80b2\u59d4\u5458\u4f1a"),
        ("2020","\u6bd5\u4e1a\u5178\u793c\u4ee3\u8868\u53d1\u8a00 \u2014 \u534e\u4e1c\u7406\u5de5\u5927\u5b66"),
        ("2019","\u5168\u56fd\u4e00\u7b49\u5956 \u2014 FPGA\u76f2\u4eba\u5bfc\u822a \u2014 \u201c\u6311\u6218\u676f\u201d\u5168\u56fd\u5927\u5b66\u751f\u8bfe\u5916\u5b66\u672f\u79d1\u6280\u4f5c\u54c1\u7ade\u8d5b"),
        ("2018","\u5168\u56fd\u91d1\u5956 \u2014 \u4eab\u73a9 \u2014 \u201c\u521b\u9752\u6625\u201d\u4e2d\u56fd\u9752\u5e74\u521b\u65b0\u521b\u4e1a\u5927\u8d5b"),
        ("2017","\u56fd\u5bb6\u5956\u5b66\u91d1 (\u524d0.2%, \u00a58,000) \u2014 \u4e2d\u534e\u4eba\u6c11\u5171\u548c\u56fd\u6559\u80b2\u90e8"),
        ("2016\u20132019","\u6210\u601d\u5371\u540d\u8a89\u6821\u957f\u5956\u5b66\u91d1 (\u524d1%) \u2014 \u534e\u4e1c\u7406\u5de5\u5927\u5b66"),
        ("2016\u20132019","\u7279\u7b49\u5b66\u4e1a\u5956\u5b66\u91d1 \u2014 \u4e13\u4e1a\u7b2c\u4e00\uff0c\u8fde\u7eed5\u5b66\u671f \u2014 \u534e\u4e1c\u7406\u5de5\u5927\u5b66"),
    ]: entry(y, [P(d)], sp=2)

    # ---- \u4ee3\u8868\u6027\u521b\u4f5c ----
    section("\u4ee3\u8868\u6027\u521b\u4f5c\u4f5c\u54c1")
    for y, d in [
        ("2025",f'<font name="{B}">Roller-Skating Knight</font> \u2014 3D\u6e38\u620f\u9879\u76ee\u3002Rookie Awards A\u7ea7\u3002'),
        ("2025",f'<font name="{B}">Situated Bodies, Wandering Minds</font> \u2014 ACM SIGGRAPH 2025\uff0c\u6e29\u54e5\u534e BOF\u4e13\u573a\u3002'),
        ("2024",f'<font name="{B}">AR Game for Maison Margiela</font> \u2014 AR\u624b\u673a\u6e38\u620f\uff0cReplica\u9999\u6c34\u7cfb\u5217\u3002'),
        ("2024",f'<font name="{B}">The Struggle</font> \u2014 3D\u52a8\u753b\u3002Rookie Awards A\u7ea7\u3002'),
        ("2024",f'<font name="{B}">Ganesha</font> \u2014 \u89c6\u89c9\u7279\u6548\u9879\u76ee\u3002Rookie Awards A\u7ea7\u3002'),
        ("2023",f'<font name="{B}">\u7fbd\u67f1</font> \u2014 \u827a\u672f\u88c5\u7f6e\uff0c\u540c\u6d4e\u5927\u5b66\u3002'),
        ("2022",f'<font name="{B}">\u6c89\u6d78\u5f0f\u6c7d\u8f66\u7a7a\u95f4</font> \u2014 \u6570\u5b57\u5a92\u4f53\u88c5\u7f6e\uff0c\u5927\u4f17\u9014\u9510\u4e0a\u5e02\u53d1\u5e03\u4f1a\u3002'),
        ("2021",f'<font name="{B}">\u6d77\u6d0b\u7684\u6545\u4e8b</font> \u2014 3D\u52a8\u753b\u3002IOAF\u94dc\u5956\u3002'),
    ]: entry(y, [P(d)], sp=2)

    # ---- BUILD ----
    def on_first(canvas, doc): pass
    def on_later(canvas, doc):
        canvas.saveState()
        canvas.setFont(FONT_R, 8)
        canvas.setFillColor(HexColor('#888888'))
        canvas.drawString(MARGIN, PAGE_H - 0.45*inch, "\u7b80\u5386")
        canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.45*inch, f"\u5f90\u56ed\u56ed  {doc.page}")
        canvas.restoreState()

    doc.build(story, onFirstPage=on_first, onLaterPages=on_later)
    print(f"Chinese CV generated successfully: {OUTPUT_PATH}")

if __name__ == "__main__":
    build_cv()
