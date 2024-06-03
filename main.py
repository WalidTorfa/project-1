import streamlit as st
from custom_pdf import PDF as custom_pdf
from fpdf import FPDF
import os
from data import *

# Custom CSS to center align text areas
st.markdown("""
    <style>
    .center-align {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .center-align > div {
        width: 50%; /* Adjust the width as per your requirement */
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Generate PDF from Metadata")

# Center align the text areas
with st.container():
    st.markdown('<div class="center-align">', unsafe_allow_html=True)
    template_name = st.selectbox("Choose the proper template", ("template 1", "template2"))
    contract_number = st.text_input("Contract Number")
    date = st.date_input("Date")
    destination = st.text_input("Destination")
    invoice_name = st.text_area("Invoice Name")
    product = st.text_area("Product")
    origin = st.text_input("Origin")
    producer = st.text_input("Producer")
    exporter = st.text_input("Exporter")
    BL_name = st.text_area("BL Name")
    BL_notify_name = st.text_area("BL Notify Name")
    notes = st.text_area("Notes")
    st.markdown('</div>', unsafe_allow_html=True)

if st.button("Generate PDF"):
    entries = {
        "contract_number": contract_number,
        "date": date.strftime("%Y-%m-%d"),
        "destination": destination,
        "invoice_name": invoice_name,
        "product": product,
        "origin": origin,
        "producer": producer,
        "exporter": exporter,
        "BL_name": BL_name,
        "BL_notify_name": BL_notify_name,
        "notes": notes
    }

    text = pdf_data(template_name, entries)
    generate_pdf(text, entries)

    with open("document.pdf", "rb") as pdf_file:
        st.download_button("Download PDF", pdf_file, "document.pdf")
