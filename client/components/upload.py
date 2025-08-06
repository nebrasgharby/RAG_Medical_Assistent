import streamlit as st
from utils.api import upload_pdfs_api


# In upload.py
def render_uploader():
    st.sidebar.header("Upload Medical documents (.PDFs)")
    uploaded_files = st.sidebar.file_uploader(
        "Upload multiple PDFs",
        type="pdf",
        accept_multiple_files=True
    )
    
    if uploaded_files and st.sidebar.button("Upload DB"):
        try:
            # Reset file pointers before reading
            files = [(f.name, f.getvalue()) for f in uploaded_files]
            response = upload_pdfs_api(uploaded_files)
            
            if response.status_code == 200:
                st.sidebar.success("Uploaded successfully")
            else:
                st.sidebar.error(f"Error: {response.text}")
        except Exception as e:
            st.sidebar.error(f"Connection failed: {str(e)}")