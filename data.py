from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
import os
from fpdf import FPDF
from custom_pdf import PDF as custom_pdf
from templates import get_template

def pdf_data(template_name, entries):
    template = get_template(entries, template_name)
    return template

def generate_pdf(text, metadata):
    pdf = custom_pdf()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    # Adding the main title
    pdf.chapter_title(f"Required Documents For S/C No. {metadata['contract_number']} on {metadata['date']} TO {metadata['destination']}:")

    # Adding the text content
    pdf.chapter_body(text)

    # Save the PDF
    pdf.output("document.pdf")
