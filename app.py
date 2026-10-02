import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="Education AI",
    page_icon="📚"
)

st.title("📚 Education AI")
st.write("Upload your college PDF and ask questions about it.")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file:
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    st.success("PDF uploaded successfully! ✅")

    st.subheader("📄 Extracted Text")

    st.text_area(
        "PDF Content",
        text,
        height=300
    )