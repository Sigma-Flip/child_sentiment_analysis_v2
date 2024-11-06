from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(keyNum, date, summary, evaluation, analysis, tl):
    file_path = f"{keyNum}_{date}_report.pdf"
    c = canvas.Canvas(file_path, pagesize=A4)
    c.drawString(100, 800, f"Report for {date}")
    c.drawString(100, 780, f"Summary: {summary}")
    c.drawString(100, 760, f"Evaluation: {evaluation}")
    c.drawString(100, 740, f"Analysis: {analysis}")
    c.drawString(100, 720, f"Timeline Summary: {tl}")
    c.save()
    return file_path
