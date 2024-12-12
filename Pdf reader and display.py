import streamlit as st
import fitz
from io import BytesIO
from PIL import Image

def display_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    num_pages = doc.page_count
    
    for page_num in range(num_pages):
        page = doc.load_page(page_num)  
        pix = page.get_pixmap() 
        
        
        img = Image.open(BytesIO(pix.tobytes("png")))
        
       
        st.image(img, caption=f"Page {page_num + 1}", use_column_width=True)

st.title("PDF READER")

pdf_file = st.file_uploader("Upload a PDF", type="pdf")

if pdf_file is not None:
    display_pdf(pdf_file)

