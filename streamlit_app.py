import streamlit as st
import zipfile, io, os, random, string
from datetime import datetime

st.set_page_config(page_title="Python Automation Pack", page_icon="⚙️", layout="centered")

st.title("⚙️ Python Automation Pack – 10 Ready-to-Use Scripts")
st.write("Select automation scripts, and download your ready-to-use Python tools instantly!")

# List of available scripts
scripts = {
    "Excel Report Generator": """import pandas as pd
import random

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Score': [random.randint(60,100) for _ in range(3)]}
df = pd.DataFrame(data)
df.to_excel('report.xlsx', index=False)
print('Excel report generated successfully!')
""",

    "PDF Merger": """from PyPDF2 import PdfMerger

pdfs = ['file1.pdf', 'file2.pdf']
merger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)
merger.write('merged.pdf')
merger.close()
print('PDF merged successfully!')
""",

    "File Organizer": """import os, shutil

folder = '.'
extensions = {'Images': ['.jpg', '.png'], 'Docs': ['.pdf', '.txt']}
for file in os.listdir(folder):
    for key, exts in extensions.items():
        if file.endswith(tuple(exts)):
            os.makedirs(key, exist_ok=True)
            shutil.move(file, key + '/' + file)
print('Files organized successfully!')
""",

    "Weather Fetcher": """import requests

API_KEY = 'your_api_key'
city = input('Enter city: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
response = requests.get(url).json()
print(f"Weather in {city}: {response['main']['temp']}°C")
""",

    "Email Sender": """import smtplib
from email.mime.text import MIMEText

sender = 'youremail@gmail.com'
password = 'yourpassword'
receiver = input('Enter recipient email: ')
msg = MIMEText('This is a test email from Python Automation Pack.')
msg['Subject'] = 'Test Email'
msg['From'] = sender
msg['To'] = receiver

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
print('Email sent successfully!')
""",

    "Screenshot Tool": """import pyautogui
image = pyautogui.screenshot()
image.save('screenshot.png')
print('Screenshot saved as screenshot.png')
""",

    "QR Code Generator": """import qrcode
text = input('Enter text to generate QR code: ')
img = qrcode.make(text)
img.save('qrcode.png')
print('QR Code saved as qrcode.png')
""",

    "Web Scraper": """import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
for heading in soup.find_all('h2'):
    print(heading.text)
""",

    "Text-to-Speech": """from gtts import gTTS
text = input('Enter text: ')
tts = gTTS(text)
tts.save('speech.mp3')
print('Text converted to speech!')
""",

    "Duplicate File Remover": """import os, hashlib

def file_hash(filename):
    h = hashlib.md5()
    with open(filename, 'rb') as f:
        chunk = f.read()
        h.update(chunk)
    return h.hexdigest()

folder = '.'
hashes = {}
for file in os.listdir(folder):
    if os.path.isfile(file):
        h = file_hash(file)
        if h in hashes:
            os.remove(file)
        else:
            hashes[h] = file
print('Duplicate files removed!')
"""
}

# UI - Script selection
selected = st.multiselect("🧠 Choose scripts to include:", list(scripts.keys()))

if st.button("📦 Generate ZIP File"):
    if not selected:
        st.warning("Please select at least one script.")
    else:
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as z:
            for name in selected:
                z.writestr(name.replace(" ", "_").lower() + ".py", scripts[name])
            z.writestr("README.txt", "Generated with Python Automation Pack")

        st.success("✅ ZIP file generated successfully!")
        st.download_button("⬇️ Download Automation Pack", buffer.getvalue(),
                           file_name="python_automation_pack.zip", mime="application/zip")

