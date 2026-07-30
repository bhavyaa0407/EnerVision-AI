from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import inch
from reportlab.lib import colors

from datetime import datetime
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(
    TTFont(
        "DejaVu",
        "Python_Code/Fonts/dejavu-sans-ttf-2.37/ttf/DejaVuSans.ttf"
    )
)
# ==========================================================
# BRAND
# ==========================================================

PRODUCT_NAME = "EnerVision AI"
TAGLINE = "AI Powered Smart Energy Audit Platform"
REPORT_TITLE = "Industrial Energy Audit Report"

# ==========================================================
# COLORS
# ==========================================================

NAVY = colors.HexColor("#0F172A")
BLUE = colors.HexColor("#2563EB")
GREEN = colors.HexColor("#10B981")
RED = colors.HexColor("#DC2626")
ORANGE = colors.HexColor("#F59E0B")

BACKGROUND = colors.HexColor("#F8FAFC")
CARD = colors.white
BORDER = colors.HexColor("#D9E2EC")

TEXT = colors.HexColor("#1F2937")
LIGHT = colors.HexColor("#64748B")

# ==========================================================
# STYLES
# ==========================================================

styles = getSampleStyleSheet()

TITLE_STYLE = ParagraphStyle(
    "TITLE",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontName="DejaVu",
    fontSize=24,
    leading=30,
    textColor=colors.white,
)

TAG_STYLE = ParagraphStyle(
    "TAG",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontName="DejaVu",
    fontSize=11,
    textColor=LIGHT,
)

SECTION_STYLE = ParagraphStyle(
    "SECTION",
    parent=styles["Heading2"],
    fontName="DejaVu",
    fontSize=16,
    textColor=NAVY,
    spaceBefore=8,
    spaceAfter=10,
)

BODY_STYLE = ParagraphStyle(
    "BODY",
    parent=styles["BodyText"],
    fontName="DejaVu",
    fontSize=10,
    leading=18,
    textColor=TEXT,
)
SUBTITLE_STYLE = ParagraphStyle(
    "Subtitle",
    parent=styles["Normal"],
    fontName="DejaVu",
    fontSize=14,
    alignment=1,      # Center
    textColor=colors.HexColor("#5F6F8C"),
    spaceAfter=8
)

CARD_TITLE = ParagraphStyle(
    "CARD_TITLE",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontName="DejaVu",
    fontSize=10,
    textColor=colors.white,
)

CARD_VALUE = ParagraphStyle(
    "CARD_VALUE",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontName="DejaVu",
    fontSize=22,
    textColor=colors.white,
)

CARD_UNIT = ParagraphStyle(
    "CARD_UNIT",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontName="DejaVu",
    fontSize=10,
    textColor=colors.white,
)

# ==========================================================
# MAIN FUNCTION
# ==========================================================

def generate_report(
    filename,
    company,
    location,
    auditor,
    industry,
    energy,
    cost,
    co2,
    health,
    estimated_saving,
    recommendations,
):

    doc = SimpleDocTemplate(
        filename,
        leftMargin=35,
        rightMargin=35,
        topMargin=30,
        bottomMargin=30
    )

    elements = []
    report_id = "EVAI-" + datetime.now().strftime("%Y%m%d-%H%M%S")
# ==========================================================
# LOGO
# ==========================================================

    logo_path = "Python_Code/assets/home_logo.png"

    if os.path.exists(logo_path):
      logo = Image(logo_path, width=120, height=60)
      logo.hAlign = "CENTER"
      elements.append(logo)
      elements.append(Spacer(1,6))
# ==========================================================
# HEADER
# ==========================================================
    elements.append(Spacer(1, 8))
        
    elements.append(
    Paragraph(
        "AI Powered Smart Energy Audit Platform",
        SUBTITLE_STYLE
    )
)

    elements.append(Spacer(1, 6))


    elements.append(
        HRFlowable(
            width="100%",
            thickness=2,
            color=GREEN
        )
    )

    elements.append(Spacer(1,0.30*inch))

    # ==========================================================
    # EXECUTIVE INFORMATION
    # ==========================================================

    elements.append(
        Paragraph(
            "EXECUTIVE INFORMATION",
            SECTION_STYLE
        )
    )

    info = Table(
        [[
            Paragraph(
                f"""
                <font size='15'><b>Company Name</b></font>

                <br/>

                <font size='13'>{company}</font>

                <br/><br/>

                <b>Industry</b> : {industry}

                <br/>

                <b>Location</b> : {location}

                <br/>

                <b>Auditor</b> : {auditor}

                <br/>

                <b>Date</b> : {datetime.now().strftime("%d %B %Y")}

                <br/>

                <b>Time</b> : {datetime.now().strftime("%H:%M")}

                <br/>

                <b>Report ID</b> : {report_id}
                """,
                BODY_STYLE
            )
        ]],
        colWidths=[6.8*inch]
    )

    info.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),CARD),
        ("BOX",(0,0),(-1,-1),1,BORDER),
        ("TOPPADDING",(0,0),(-1,-1),18),
        ("BOTTOMPADDING",(0,0),(-1,-1),18),
        ("LEFTPADDING",(0,0),(-1,-1),20),
        ("RIGHTPADDING",(0,0),(-1,-1),20),
    ]))

    elements.append(info)

    elements.append(Spacer(1,0.35*inch))

    # ==========================================================
    # KPI DASHBOARD
    # ==========================================================

    elements.append(
        Paragraph(
            "EXECUTIVE DASHBOARD",
            SECTION_STYLE
        )
    )

    def create_card(title, value, unit, color):

        t = Table(
            [[
                Paragraph(
                 f"""<para align="center">
                 <font size="10"><b>{title}</b></font><br/><br/>
                 <font size="22"><b>{str(value).strip()}</b></font><br/>
                 <font size="10">{unit}</font>
                </para>""",
                ParagraphStyle(
                 "Card",
                  fontName="DejaVu",
                  alignment=TA_CENTER,
                  textColor=colors.white,
                  leading=18,
    ),
)
            ]],
            colWidths=[3.2*inch],
            rowHeights=[1.18*inch]
        )

        t.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,-1),color),
            ("BOX",(0,0),(-1,-1),0,color),
            ("VALIGN",(0,0),(-1,-1),"MIDDLE")
        ]))

        return t

    health_color = GREEN

    if health.lower()=="good":
        health_color = BLUE

    elif health.lower()=="warning":
        health_color = ORANGE

    elif health.lower()=="critical":
        health_color = RED

    card1 = create_card(
        "ENERGY",
        f"{energy:.2f}",
        "Wh",
        NAVY
    )

    card2 = create_card(
        "COST",
        f"₹ {cost:.2f}",
        "",
        BLUE
    )

    card3 = create_card(
        "CO₂",
        f"{co2:.2f}",
        "kg",
        GREEN
    )
    print("Health sent to PDF:", repr(health))
    card4 = create_card(
        "HEALTH",
        "Warning",
         "",
        health_color
    )

    dashboard = Table(

        [
            [card1,card2],
            [card3,card4]
        ],

        colWidths=[3.35*inch,3.35*inch]

    )

    dashboard.setStyle(

        TableStyle([

            ("TOPPADDING",(0,0),(-1,-1),10),

            ("BOTTOMPADDING",(0,0),(-1,-1),10)

        ])

    )

    elements.append(dashboard)

    elements.append(Spacer(1,0.35*inch))

    elements.append(
    Paragraph(
        "EXECUTIVE SUMMARY",
        SECTION_STYLE
    )
)

    summary = f"""
EnerVision AI analysed the operational data and estimated an
energy consumption of <b>{energy:.2f} Wh</b>.

The current equipment health status is
<b>{health}</b>.

The estimated electricity cost is
<b>₹ {cost:.2f}</b> while the associated
carbon emission is
<b>{co2:.2f} kg</b>.

The audit indicates that implementing the recommended actions
can improve overall energy efficiency and reduce operational
expenses.
"""

    elements.append(
    Paragraph(summary, BODY_STYLE)
)

    elements.append(Spacer(1,0.25*inch))

    # ==========================================================
    # AI RECOMMENDATIONS
    # ==========================================================

    elements.append(
        Paragraph(
            "AI RECOMMENDATIONS",
            SECTION_STYLE
        )
    )

    if not recommendations:
        recommendations = [
            "No major energy optimization recommendations. The facility appears to be operating efficiently."
        ]

    for rec in recommendations:

        box = Table(
    [
        [
            Paragraph(
                f"<b>✔</b> {rec}",
                BODY_STYLE
            )
        ]
    ],
    colWidths=[6.8 * inch]
)

        box.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#F8FAFC")),
            ("BOX",(0,0),(-1,-1),1,BORDER),
            ("TOPPADDING",(0,0),(-1,-1),14),
            ("BOTTOMPADDING",(0,0),(-1,-1),14),
            ("LEFTPADDING",(0,0),(-1,-1),15),
            ("RIGHTPADDING",(0,0),(-1,-1),15),
        ]))

        elements.append(box)
        elements.append(Spacer(1,0.12*inch))
    # ==========================================================
    # SAVINGS
    # ==========================================================

    saving = Table(
        [[
            Paragraph(
                f"""
                <para align='center'>
                <font size='12'><b>Estimated Monthly Savings</b></font>

                <br/><br/>

                <font size='28'><b>₹ {estimated_saving:.2f}</b></font>
                <font size='10'>
                Approximate Monthly Savings
                </font>

                </para>
                """,
                ParagraphStyle(
                    "Saving",
                    fontName="DejaVu",
                    alignment=TA_CENTER,
                    textColor=colors.white
                )
            )
        ]],
        colWidths=[6.8*inch]
    )

    saving.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),GREEN),
        ("TOPPADDING",(0,0),(-1,-1),18),
        ("BOTTOMPADDING",(0,0),(-1,-1),18),
    ]))

    elements.append(saving)

    elements.append(Spacer(1,0.30*inch))


    # ==========================================================
    # FOOTER
    # ==========================================================

    elements.append(
        HRFlowable(
            width="100%",
            thickness=1,
            color=BORDER
        )
    )

    elements.append(Spacer(1,0.15*inch))

    footer = Paragraph(
        f"""
        <para align='center'>

        <font size='11'><b>{PRODUCT_NAME}</b></font>

        <br/>

        <font size='9'>{TAGLINE}</font>

        <br/><br/>

        <font size='8' color='#64748B'>
        Generated on {datetime.now().strftime("%d %B %Y %H:%M")}
        Report ID : {report_id}
        Confidential Energy Audit Report
        </font>

        </para>
        """,
        BODY_STYLE
    )

    elements.append(footer)

    # ==========================================================
    # CREATE PDF
    # ==========================================================

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    elements.append(Spacer(1,6))
    doc.build(elements)

    return filename