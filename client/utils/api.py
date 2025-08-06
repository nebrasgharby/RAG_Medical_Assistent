
import requests
from config import API_URL
import streamlit as st

def upload_pdfs_api(files):
    try:
        files_payload = [("files", (f.name, f.getvalue(), "application/pdf")) for f in files]
        response = requests.post(
            f"{API_URL}/upload_pdfs/",
            files=files_payload,
            timeout=10  # Add timeout
        )
        response.raise_for_status()  # Raises exception for 4XX/5XX
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"API Connection Error: {str(e)}")
        return None
def ask_question(question):
    return requests.post(f"{API_URL}/ask/",data={"question":question})