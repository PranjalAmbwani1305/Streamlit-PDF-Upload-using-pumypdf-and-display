import streamlit as st
import fitz

def main():
    st.title("PDF Processor")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Access the uploaded file name (path)
        file_path = uploaded_file.name
        with open(file_path, "rb") as f:
            doc = fitz.open(f)

            # Process the PDF document
            for page_num in range(doc.page_count):
                page = doc[page_num]
                # Example: Extract text from the page
                text = page.get_text()
                st.write(f"Page {page_num + 1} Text:")
                st.write(text)

                # Example: Convert page to image
                pix = page.get_pixmap()
                st.image(pix.tobytes())

if __name__ == "__main__":
    main()
