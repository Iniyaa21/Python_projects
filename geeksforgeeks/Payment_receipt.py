from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors

pdf = SimpleDocTemplate("example.pdf", pagesize=A4)

styles = getSampleStyleSheet()
style = styles["Heading1"]
style.alignment = 1

title = "Payment receipt"
title = Paragraph(title, style=style)

DATA = [
    ["Date", "Name", "Subscription", "Price (Rs.)"],
    [
        "16/11/2020",
        "Full Stack Development with React & Node JS - Live",
        "Lifetime",
        "10,999.00/-",
    ],
    ["16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"],
    ["Sub Total", "", "", "20,9998.00/-"],
    ["Discount", "", "", "-3,000.00/-"],
    ["Total", "", "", "17,998.00/-"],
]

tablestyle = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (4, 4), 1, colors.black),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.darkblue),
        ("ALIGN", (0, 0), (-1, -1), "CENTER")
    ]
)

table = Table(DATA, style=tablestyle)

pdf.build([title, table])
