import streamlit as st
import fitz

def main():
    st.title("PDF Viewer App")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        pdf_bytes = uploaded_file.read()
        pdf_document = fitz.open(stream=pdf_bytes)

        st.write(f"Total Pages: {len(pdf_document)}")

        page_number = st.number_input(
            "Select page number",
            min_value=1,
            max_value=len(pdf_document),
            value=1
        )

        page = pdf_document[page_number - 1]
        pix = page.get_pixmap()
        img_bytes = pix.tobytes()

        st.image(img_bytes, caption=f"Page {page_number}", use_column_width=True)

        pdf_document.close()

if __name__ == "__main__":
    main()
