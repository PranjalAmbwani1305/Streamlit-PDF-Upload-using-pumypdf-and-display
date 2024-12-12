import streamlit as st
import fitz

def main():
    st.title("PDF Viewer App ")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
       
        pdf_bytes = uploaded_file.read()
        pdf_document = fitz.open(stream=pdf_bytes)

   
        total_pages = len(pdf_document)
        st.write(f"Total Pages: {total_pages}")

     
        for page_number in range(total_pages):
            
            page = pdf_document[page_number]

           
            pix = page.get_pixmap()

          
            img_bytes = pix.tobytes()

            
            st.image(img_bytes, use_column_width=True)

      
        pdf_document.close()

if __name__ == "__main__":
    main()
