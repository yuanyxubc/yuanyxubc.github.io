"""
Generate Yuanyuan Xu's Academic CV PDF (English) — elegant sans-serif edition.
Uses Calibri (with Segoe UI / Helvetica fallback), centered headers, date-column layout.
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

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "YuanyuanXu_CV.pdf")

# --- Register elegant sans-serif fonts ---
FONT_DIR = "C:/Windows/Fonts"

def try_register(name, filenames, subfont=0):
    for fn in filenames:
        p = os.path.join(FONT_DIR, fn)
        if os.path.exists(p):
            try:
                pdfmetrics.registerFont(TTFont(name, p, subfontIndex=subfont))
                return True
            except:
                pass
    return False

# Try Calibri first (elegant, modern), then Segoe UI, then Helvetica (built-in)
has_calibri = (
    try_register('SansRegular', ['calibri.ttf', 'Calibri.ttf']) and
    try_register('SansBold', ['calibrib.ttf', 'Calibri Bold.ttf', 'calibri-bold.ttf']) and
    try_register('SansItalic', ['calibrii.ttf', 'Calibri Italic.ttf', 'calibri-italic.ttf'])
)

if not has_calibri:
    has_segoe = (
        try_register('SansRegular', ['segoeui.ttf', 'SegoeUI.ttf']) and
        try_register('SansBold', ['segoeuib.ttf', 'SegoeUI-Bold.ttf']) and
        try_register('SansItalic', ['segoeuii.ttf', 'SegoeUI-Italic.ttf'])
    )
    if not has_segoe:
        # Fallback to Helvetica (built-in)
        class _Alias:
            pass
        FONT_R, FONT_B, FONT_I = 'Helvetica', 'Helvetica-Bold', 'Helvetica-Oblique'
    else:
        FONT_R, FONT_B, FONT_I = 'SansRegular', 'SansBold', 'SansItalic'
else:
    FONT_R, FONT_B, FONT_I = 'SansRegular', 'SansBold', 'SansItalic'

print(f"Using font: {FONT_R}")

MARGIN = 0.85 * inch
PAGE_W, PAGE_H = letter

# Elegant color palette
DARK = HexColor('#1a1a2e')
ACCENT = HexColor('#2D5A3D')
RULE_COLOR = HexColor('#999999')

styles = {
    'name': ParagraphStyle('Name', fontName=FONT_B, fontSize=18, alignment=TA_CENTER, spaceAfter=2, textColor=DARK, leading=22),
    'contact': ParagraphStyle('Contact', fontName=FONT_R, fontSize=9.5, alignment=TA_CENTER, leading=14, spaceAfter=4, textColor=HexColor('#444444')),
    'section': ParagraphStyle('Section', fontName=FONT_B, fontSize=11, alignment=TA_LEFT, spaceBefore=14, spaceAfter=6, textColor=DARK, leading=14),
    'subsection': ParagraphStyle('Subsection', fontName=FONT_B, fontSize=9.5, alignment=TA_LEFT, spaceBefore=8, spaceAfter=3, textColor=HexColor('#333333')),
    'entry_title': ParagraphStyle('EntryTitle', fontName=FONT_B, fontSize=9.5, leading=12.5, textColor=DARK),
    'entry_body': ParagraphStyle('EntryBody', fontName=FONT_R, fontSize=9.5, leading=12.5, textColor=HexColor('#333333')),
    'entry_italic': ParagraphStyle('EntryItalic', fontName=FONT_I, fontSize=9.5, leading=12.5, textColor=HexColor('#555555')),
    'date': ParagraphStyle('Date', fontName=FONT_R, fontSize=9, leading=12.5, textColor=HexColor('#666666')),
}

DATE_COL = 1.1 * inch
DETAIL_COL = PAGE_W - 2*MARGIN - DATE_COL - 0.1*inch

def build_cv():
    doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=0.7*inch, bottomMargin=0.7*inch)

    story = []

    # ---- HEADER ----
    story.append(Paragraph("YUANYUAN XU", styles['name']))
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width="100%", thickness=0.8, color=RULE_COLOR, spaceAfter=6))
    story.append(Paragraph(
        "Ph.D. Student, Interdisciplinary Studies<br/>"
        "Faculty of Creative &amp; Critical Studies, University of British Columbia",
        styles['contact']))
    story.append(HRFlowable(width="100%", thickness=0.4, color=RULE_COLOR, spaceBefore=2, spaceAfter=8))

    def section(title):
        story.append(HRFlowable(width="100%", thickness=0.3, color=HexColor('#cccccc'), spaceBefore=4, spaceAfter=0))
        story.append(Paragraph(title.upper(), styles['section']))

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
        t = f'{authors}. <b>"{title}."</b> <i>{venue}</i>.'
        if doi: t += f' <font color="#2D5A3D">{doi}</font>'
        return P(t)

    # ---- EDUCATION ----
    section("Education")
    entry("2025 \u2013 2029", [
        P("<b>Ph.D. in Interdisciplinary Studies</b>",'entry_title'),
        P("<i>University of British Columbia</i>",'entry_italic'),
        P("Faculty of Creative &amp; Critical Studies. Co-supervised by Prof. Aleksandra Dulic (Professor, FCCS) and Prof. Patricia Lasserre (Associate Professor, Computer Science). Research: co-designing educational games with Indigenous communities for environmental resilience. Fully funded: OGRS (CAD $25,000/year) and IDPT tuition award.")
    ])
    entry("2020 \u2013 2023", [
        P("<b>M.Eng. in Design</b>",'entry_title'),
        P("<i>Tongji University, Shanghai \u2014 College of Design and Innovation</i>",'entry_italic'),
        P("Full Scholarship (\u00a532,000). Graduate Commencement Speaker (2023).")
    ])
    entry("2016 \u2013 2020", [
        P("<b>B.A. in Product Design</b>",'entry_title'),
        P("<i>East China University of Science and Technology, Shanghai</i>",'entry_italic'),
        P("GPA: 3.7/4.0, Rank first in major for 4 consecutive years. National Scholarship (Top 0.2%, \u00a58,000). Cheng Si-wei Honorary Principal's Scholarship (Top 1%). Grand Prize Academic Scholarship (5 consecutive semesters). Person of the Year Nominee. Role Model Ambassador. Shanghai Outstanding Graduate (Top 2%). Graduate Commencement Speaker (2020).")
    ])
    entry("2023 \u2013 2025", [
        P("<b>Diploma in Game Design, Animation, and VFX</b>",'entry_title'),
        P("<i>Think Tank Training Centre, Vancouver</i>",'entry_italic'),
        P("Full-cycle game production pipeline: 3D animation, VFX, and game design.")
    ])

    # ---- RESEARCH POSITIONS ----
    section("Research Positions")
    entry("Sep 2025 \u2013 present", [
        P("<b>Research Assistant \u2014 Center for Culture and Technology</b>",'entry_title'),
        P("<i>University of British Columbia</i>",'entry_italic'),
        P("Beaver Worlds Project: participatory game design for Okanagan water governance and Indigenous knowledge mobilisation.")
    ])

    # ---- PUBLICATIONS ----
    section("Publications")

    subsec("Journal Articles")
    for a,t,v,d in [
        ("<b>Y. Xu</b>, Z. Sun, C. Zhen, Y.-S. Lin, T.H. Sarker, M. Thorogood, P. Lasserre, A. Dulic","From Engagement to Resilience: A Systematic Review of Game-Based Learning for Environmental Resilience","Sustainability, 18(5), 2305, 2026","doi.org/10.3390/su18052305"),
        ("<b>Y. Xu*</b>, X. Shan, M. Guo, W. Gao, Y.-S. Lin","Design and Application of Experience Management Tools from the Perspective of Customer Perceived Value","World Electric Vehicle Journal, 15(8), 378, 2024","doi.org/10.3390/wevj15080378"),
        ("<b>Y. Xu*</b>, W. Gao, Y. Wang, X. Shan, Y.-S. Lin","Enhancing User Experience and Trust in Advanced LLM-Based Conversational Agents","Computing and Artificial Intelligence, 2(2), 1467, 2024","doi.org/10.59400/cai.v2i2.1467"),
        ("<b>Y. Xu*</b>, Y.-S. Lin, X. Zhou, X. Shan","Utilizing Emotion Recognition Technology to Enhance User Experience in Real-Time","Computing and Artificial Intelligence, 2(1), 1388, 2024","doi.org/10.59400/cai.v2i1.1388"),
        ("M. Liu*, M. Guo, L. Jiang, <b>Y. Xu</b>","Kansei Engineering\u2013Based Product Form Design: Eye-Tracking on Drinkware","Journal of the University of Shanghai, 42(5), 2020","doi.org/10.13255/j.cnki.jusst.20191122008"),
        ("<b>Y. Xu*</b>, Y. Bao, B. Yang","Design Analysis of Therapeutic Toys for Children with Autism","Art and Technology, 2018",None),
        ("M. Liu*, M. Guo, L. Jiang, <b>Y. Xu</b>","Exploring the Relationship Between Eye-Tracking Data and Product Form Design","Literature Life, 2019","doi.org/10.3969/j.issn.1005-5312.2019.10.029"),
    ]: entry("", [pub(a,t,v,d)], sp=3)

    subsec("Conference Papers &amp; Book Chapters")
    for a,t,v,d in [
        ("<b>Y. Xu*</b>, X. Shan, Y.-S. Lin, J. Wang","AI-Enhanced Tools for Cross-Cultural Game Design","HCII 2024, LNCS 15377, Springer, 2025","doi.org/10.1007/978-3-031-76812-5_29"),
        ("X. Shan, <b>Y. Xu*</b>, Y. Wang, Y.-S. Lin, Y. Bao","Cross-Cultural Implications of Large Language Models","HCII 2024, LNCS 15375, Springer, 2025","doi.org/10.1007/978-3-031-76806-4_8"),
        ("T. Xia*, <b>Y. Xu</b>, X. Shan","KOA-Monitor: A Digital Intervention and Functional Assessment System","HCII 2025, LNCS 15810, Springer, 2025","doi.org/10.1007/978-3-031-92710-2_26"),
        ("X. Shan, <b>Y. Xu*</b>, Y. Wang, T. Xia, Y.-S. Lin","Designing Wine Tasting Experiences for All","HCII 2025, CCIS 2772, Springer, 2026","doi.org/10.1007/978-3-032-12767-9_42"),
        ("X. Shan, <b>Y. Xu</b>, T. Xia, Y.-S. Lin","Rethinking Wine Tasting for Chinese Consumers","2025 IEEE International Conference on Content-Based Multimedia Indexing (CBMI), 2025",None),
        ("<b>Y. Xu*</b>, Y.-S. Lin","Exploring the Influence of User-Perceived Value on NEV-Enterprises","FFIT 2024, Atlantis Press, 2024","doi.org/10.2991/978-94-6463-572-0_2"),
        ("G. Tian, <b>Y. Xu*</b>","A Study on the Typeface Design Method of Han Characters Imitated Tangut","AEHSSR, 2022","doi.org/10.56028/aehssr.2.1.270"),
    ]: entry("", [pub(a,t,v,d)], sp=3)

    subsec("Forthcoming (In Press)")
    for a,t,v in [
        ("<b>Y. Xu</b>, Z. Sun, C. Zhen, Y.-S. Lin, M. Thorogood, M. Smith, P. Lasserre, A. Dulic","Mapping Ecological Empathy: A Semantic Network Analysis of Player Perceptions in 3D Environmental Education Games","HCII 2026, LNCS, Springer"),
        ("C. Zhen, <b>Y. Xu</b>, C.S. Souto, Z. Sun, P. Lasserre, A. Dulic, M. Thorogood","Animation Design Philosophy in 3D Educational Games: The Development of Beaver Worlds","HCII 2026, CCIS, Springer"),
        ("Z. Sun, <b>Y. Xu</b>, C. Zhen, Y.-S. Lin, M. Thorogood, P. Lasserre, A. Dulic, M. Smith","Struggle as Flow: Challenge, Design, and Experience in Soulslike Games","HCII 2026, LNCS, Springer"),
        ("<b>Y. Xu</b>, Z. Sun, Y.-S. Lin, P. Lasserre, A. Dulic","The Absent Teacher in Eco-Games: A Theoretical Framework for Teacher Integration","DiGRA 2026"),
        ("<b>Y. Xu</b>, P. Lasserre, A. Dulic","From Resource to Kin: Designing for Environmental Resilience in the Okanagan","DiGRA 2026"),
        ("Z. Sun, <b>Y. Xu</b>, Y.-S. Lin, P. Lasserre, A. Dulic, M. Smith","Re-evaluating the Pursuit of Hyper-Realism in VR Game Design","DiGRA 2026"),
    ]: entry("", [pub(a,t,v)], sp=3)

    subsec("Patents")
    entry("2023", [P('X. Sun et al., <b>Y. Xu</b>. <b>"FPGA-Based Vision Method for Blind Navigation"</b> (CN110070514B). Chinese Patent Office. <i>Granted.</i>')])

    # ---- PRESENTATIONS ----
    section("Presentations")
    entry("Jun 2026", [P('<b>Y. Xu</b> et al. Three papers. <i>HCI International Conference (HCII) 2026, Montreal.</i>')])
    entry("Jun 2026", [P('<b>Y. Xu</b> et al. Doctoral Consortium and Education Session. <i>Digital Games Research Association Conference (DiGRA) 2026, Ireland.</i>')])
    entry("2025", [P('<b>Y. Xu</b>, Y.-S. Lin. "Situated Bodies, Wandering Minds." <i>ACM SIGGRAPH Conference on Computer Graphics and Interactive Techniques (SIGGRAPH) 2025, Vancouver \u2014 Birds of a Feather (BOF) Session.</i>')])
    entry("2024", [P('<b>Y. Xu</b>. "Creativity for Sensational Perception." <i>HCI International Conference (HCII) 2024, Washington DC.</i>')])
    entry("2023", [P('<b>Y. Xu</b>. Graduate Commencement Speech. <i>Tongji University.</i>')])
    entry("2020", [P('<b>Y. Xu</b>. Graduate Commencement Speech. <i>East China University of Science and Technology.</i>')])

    # ---- GRANTS ----
    section("Research Grants &amp; Fellowships")
    entry("2025", [
        P("<b>Okanagan Graduate Research Scholarship (OGRS) + International Doctoral Partial Tuition Award (IDPT)</b>",'entry_title'),
        P('University of British Columbia. 4-year doctoral funding.')
    ])
    entry("2022", [
        P("<b>Shanghai Technology Entrepreneurship Foundation (EFG) \u2014 RMB 500,000</b>",'entry_title'),
        P('PI. "Designing Childhood: Play, Emotion, and Soft Toys."')
    ])
    entry("2017", [P("<b>Shanghai First-Class Discipline Construction Fund</b>",'entry_title'), P('Student Researcher. "Kansei-Based User Perception Analysis."')])
    entry("2017", [P("<b>NSFC (Project No. 51905175)</b>",'entry_title'), P('Student Researcher. "Kansei Engineering Product Form Design."')])
    entry("2017", [P("<b>Shanghai College Student Innovation Program (No. X18223)</b>",'entry_title'), P('Team Leader.')])
    entry("2017", [P("<b>Shanghai Student Innovation &amp; Entrepreneurship Training (EFG)</b>",'entry_title'), P('Applicant.')])

    # ---- TEACHING ----
    section("Teaching Experience")
    entry("Jan 2026 \u2013 present", [
        P("<b>Teaching Assistant \u2014 CCS 325: AI &amp; Creativity</b>",'entry_title'),
        P("<i>University of British Columbia</i>",'entry_italic'),
        P("Grading, tutorial sessions, student feedback, facilitating activities on generative AI and creative coding.")
    ])
    entry("Dec 2025 \u2013 Feb 2026", [
        P("<b>Marker \u2014 CCS 330: Game Design</b>",'entry_title'),
        P("<i>University of British Columbia</i>",'entry_italic'),
        P("Grading assignments and providing written feedback for a game design course.")
    ])
    entry("2018 \u2013 2020", [
        P("<b>Teaching Assistant \u2014 Design Graphics (Shanghai Municipal Premium Course)</b>",'entry_title'),
        P("<i>East China University of Science and Technology</i>",'entry_italic'),
        P("Technical drawing, digital illustration, and design fundamentals.")
    ])

    # ---- INDUSTRY ----
    section("Industry Experience")
    entry("2022 \u2013 2023", [P("<b>Product Manager \u2014 iXp Program</b> \u2014 <i>SAP Labs, SAP Analytics Cloud, Shanghai</i>",'entry_title'), P("Led UX and analytics initiatives; organised workshops; facilitated demos and user testing.")])
    entry("2020", [P("<b>Product Manager Intern</b> \u2014 <i>Siemens, Intelligent Infrastructure, Shanghai</i>",'entry_title'), P("Customer training for Siemens Distribution Panel Model 8PT.")])
    entry("2020", [P("<b>UX Designer Intern</b> \u2014 <i>Shanghai Jahwa, Consumer Products</i>",'entry_title'), P("User research and UX design for consumer product digital platforms.")])
    entry("2017 \u2013 2019", [P("<b>Co-founder</b> \u2014 <i>SharePlay, Shanghai</i>",'entry_title'), P("Recreational equipment sharing platform. National Gold Award, China Youth Innovation and Entrepreneurship Competition.")])

    # ---- ACADEMIC SERVICE ----
    section("Academic Service")
    story.append(P(
        "<b>ACM Conference on Human Factors in Computing Systems (CHI)</b> \u2014 Special Recognition for Outstanding Reviewing, twice (2025)<br/>"
        "<b>ACM Conference on Designing Interactive Systems (DIS)</b> &nbsp;&nbsp; <b>ACM Creativity and Cognition (C&amp;C)</b><br/>"
        "<b>ACM Symposium on User Interface Software and Technology (UIST)</b> &nbsp;&nbsp; <b>ACM Symposium on Eye Tracking Research and Applications (ETRA)</b><br/>"
        "<b>ACM International Conference on Interactive Media Experiences (IMX)</b> &nbsp;&nbsp; <b>ACM Conference on Conversational User Interfaces (CUI)</b><br/>"
        "<b>ACM Conference on Automotive User Interfaces and Interactive Vehicular Applications (AutoUI)</b><br/>"
        "<b>IEEE International Symposium on Mixed and Augmented Reality (ISMAR)</b> &nbsp;&nbsp; <b>IEEE Conference on Virtual Reality and 3D User Interfaces (IEEE VR)</b><br/>"
        "<b>Eurographics/IEEE Conference on Visualization (EuroVis)</b><br/>"
        "<b>Computer-Aided Architectural Design Research in Asia (CAADRIA)</b> \u2014 International Review Committee Member<br/>"
        "<b>International Journal of Human-Computer Interaction (IJHCI)</b> &nbsp;&nbsp; <b>Innovation Technology Advances (ITA)</b>"
    ))
    story.append(Spacer(1, 8))

    # ---- AWARDS ----
    section("Selected Awards &amp; Honours")
    for y,d in [
        ("2025","Okanagan Graduate Research Scholarship (OGRS) \u2014 University of British Columbia, CAD $25,000/year, 4-year doctoral funding"),
        ("2025","International Doctoral Partial Tuition Award (IDPT) \u2014 University of British Columbia"),
        ("2025","Special Recognition for Outstanding Reviewing, twice \u2014 ACM Conference on Human Factors in Computing Systems (CHI)"),
        ("2025","Rookie of the Year \u2014 A Ranking (Game) \u2014 The Rookies Awards (Exceptional, Industry-Ready Skills)"),
        ("2024","Rookie of the Year \u2014 A Ranking (VFX and 3D Animation) \u2014 The Rookies Awards (Exceptional, Industry-Ready Skills)"),
        ("2023","Graduate Commencement Speaker \u2014 Tongji University"),
        ("2021","Full Scholarship (\u00a532,000) \u2014 Tongji University"),
        ("2021","Bronze Award \u2014 International Ocean Art Festival (IOAF) Starfish International Young Artists Exhibition"),
        ("2020","Shanghai Outstanding Graduate (Top 2%) \u2014 Shanghai Municipal Education Commission"),
        ("2020","Graduate Commencement Speaker \u2014 East China University of Science and Technology"),
        ("2019","National First Prize \u2014 FPGA Blind Navigation \u2014 \"Challenge Cup\" National College Students' Extracurricular Academic Science and Technology Works Competition"),
        ("2018","National Gold Award \u2014 SharePlay \u2014 \"Chuang Qingchun\" China Youth Innovation and Entrepreneurship Competition"),
        ("2017","National Scholarship (Top 0.2%, \u00a58,000) \u2014 Ministry of Education, People's Republic of China"),
        ("2016\u20132019","Cheng Si-wei Honorary Principal's Scholarship (Top 1%) \u2014 East China University of Science and Technology"),
        ("2016\u20132019","Grand Prize Academic Scholarship \u2014 First in Major, 5 semesters \u2014 East China University of Science and Technology"),
    ]: entry(y, [P(d)], sp=2)

    # ---- CREATIVE WORKS ----
    section("Selected Creative Works")
    for y,d in [
        ("2025","<b>Roller-Skating Knight</b> \u2014 3D game project. <i>Rookie Awards A Ranking.</i>"),
        ("2025","<b>Situated Bodies, Wandering Minds</b> \u2014 <i>ACM SIGGRAPH 2025, Vancouver, BOF Session.</i>"),
        ("2024","<b>AR Game for Maison Margiela</b> \u2014 AR mobile game for Replica Perfume Series."),
        ("2024","<b>The Struggle</b> \u2014 3D animation. <i>Rookie Awards A Ranking.</i>"),
        ("2024","<b>Ganesha</b> \u2014 VFX project. <i>Rookie Awards A Ranking.</i>"),
        ("2023","<b>Feather Columns</b> \u2014 Art installation, Tongji University."),
        ("2022","<b>Immersive Automotive Space</b> \u2014 Digital media installation, VW Touareg Launch."),
        ("2021","<b>The Story of the Ocean</b> \u2014 3D animation. <i>IOAF Bronze Award.</i>"),
    ]: entry(y, [P(d)], sp=2)

    # ---- BUILD ----
    def on_first(canvas, doc): pass
    def on_later(canvas, doc):
        canvas.saveState()
        canvas.setFont(FONT_I, 8)
        canvas.setFillColor(HexColor('#888888'))
        canvas.drawString(MARGIN, PAGE_H - 0.45*inch, "Curriculum Vitae")
        canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.45*inch, f"Xu  {doc.page}")
        canvas.restoreState()

    doc.build(story, onFirstPage=on_first, onLaterPages=on_later)
    print(f"CV generated successfully: {OUTPUT_PATH}")

if __name__ == "__main__":
    build_cv()
