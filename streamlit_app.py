import streamlit as st
import fitz

def main():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        file_path = uploaded_file.name
        with open(file_path, "rb") as f:
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                st.image(pix.tobytes())
                page = doc[page_num]
            
if __name__ == "__main__":
    main()
