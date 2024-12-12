import streamlit as st
import fitz

def main():
    st.title("PDF Viewer App")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Read the PDF file directly from memory
        pdf_bytes = uploaded_file.read()
        pdf_document = fitz.open(stream=pdf_bytes)

        # Display total pages
        st.write(f"Total Pages: {len(pdf_document)}")

        # Add a page selector
        page_number = st.number_input(
            "Select page number",
            min_value=1,
            max_value=len(pdf_document),
            value=1
        )

        # Display selected page
        page = pdf_document[page_number - 1]

        # Get page as an image
        pix = page.get_pixmap()

        # Convert to bytes
        img_bytes = pix.tobytes()

        # Display the page
        st.image(img_bytes, caption=f"Page {page_number}", use_column_width=True)

        # Close the PDF
        pdf_document.close()

if __name__ == "__main__":
    main()
