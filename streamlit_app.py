import streamlit as st
import os
import zipfile
from io import BytesIO

# --- PAGE SETUP ---
st.set_page_config(page_title="Python Automation Pack", page_icon="⚙️", layout="wide")
st.title("⚙️ Python Automation Pack")
st.write("Select the automation scripts you want to include, then download your ready-to-use ZIP file.")

# --- AVAILABLE SCRIPTS ---
scripts = {
    "Excel Report Generator": "Generates Excel reports from data.",
    "PDF Merger": "Combines multiple PDF files into one.",
    "File Organizer": "Sorts files in a folder by type.",
    "Weather Fetcher": "Fetches live weather data using OpenWeatherMap API.",
    "Email Sender": "Sends emails automatically using SMTP.",
    "Screenshot Tool": "Takes instant screenshots.",
    "QR Code Generator": "Creates QR codes from text or URLs.",
    "Web Scraper": "Extracts text data from a website.",
    "Text-to-Speech": "Converts text into spoken audio (MP3).",
    "Image Downloader": "Downloads images from given URLs."
}

# --- MULTISELECT ---
selected_scripts = st.multiselect("Choose your scripts:", list(scripts.keys()))

# --- DOWNLOAD BUTTON ---
if st.button("Generate ZIP File"):
    if not selected_scripts:
        st.warning("Please select at least one script.")
    else:
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zf:
            for script in selected_scripts:
                filename = script.lower().replace(" ", "_") + ".py"
                code = f"# {script}\n# Description: {scripts[script]}\n\nprint('Running {script}...')"
                zf.writestr(filename, code)

            zf.writestr("README.txt", "Python Automation Pack\n\nThis ZIP contains the following scripts:\n" + "\n".join(selected_scripts))

        zip_buffer.seek(0)
        st.download_button(
            label="📦 Download Automation Pack",
            data=zip_buffer,
            file_name="Python_Automation_Pack.zip",
            mime="application/zip"
        )
        st.success("Your automation pack is ready for download!")
