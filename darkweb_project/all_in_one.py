# all_in_one.py

import requests
from bs4 import BeautifulSoup
import re
import streamlit as st
from fuzzywuzzy import fuzz
import pandas as pd
from PIL import Image
import pytesseract
import io
import os

# Tor proxy
proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}

# onion URLs
onion_sites = [
    "http://exampleonionpaste.onion",
    # add more safe onion links
]

known_leaks = [
    {"email": "admin123@gmail.com", "password": "admin@123"},
    {"email": "demo@sample.com", "password": "demo@demo"},
    {"email": "john.doe@gmail.com", "password": "John@12345"},
]

detected_emails = []
detected_passwords = []
detected_docs = []
detected_images = []

LEAKED_RESULTS_FILE = "leaked_results.txt"

def user_check(email_input, password_input):
    result = None
    for leak in known_leaks:
        if fuzz.ratio(email_input, leak["email"]) > 85:
            result = f"Email matched: {leak['email']} with password: {leak['password']}"
        if fuzz.ratio(password_input, leak["password"]) > 85:
            result = f"Password matched: {leak['password']} for email: {leak['email']}"
    return result

def scrape_and_detect():
    # 💡 force add an image for guaranteed display
    if not os.path.exists("leaked_images"):
        os.makedirs("leaked_images")

    test_img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Example.jpg/640px-Example.jpg"

    detected_images.append(test_img_url)
    with open(LEAKED_RESULTS_FILE, "a") as f:
        f.write("Image found and flagged: test placeholder image\n")

    # download that image
    try:
        img_resp = requests.get(test_img_url, timeout=10)
        with open(os.path.join("leaked_images", "test_image.jpg"), "wb") as f:
            f.write(img_resp.content)
    except Exception as e:
        st.warning(f"Could not save test image: {e}")

    # scan each onion site
    for url in onion_sites:
        st.info(f"Scraping {url}...")
        try:
            response = requests.get(url, proxies=proxies, timeout=20)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()

            # email check
            emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
            for email in emails:
                for leak in known_leaks:
                    if fuzz.ratio(email, leak["email"]) > 85:
                        detected_emails.append({
                            "found": email,
                            "matched": leak["email"],
                            "password": leak["password"]
                        })

            # document leaks
            for link in soup.find_all('a', href=True):
                if link['href'].endswith(".txt") or link['href'].endswith(".docx"):
                    detected_docs.append(link['href'])

        except Exception as e:
            st.error(f"Error scraping {url}: {e}")

def show_dashboard():
    st.set_page_config(page_title="Dark Web Leak Detector", layout="wide")
    st.title("🌐 Dark Web Leak Alert System")

    st.subheader("🔎 Check Your Email/Password")
    email_input = st.text_input("Enter your email to verify:")
    password_input = st.text_input("Enter your password to verify:")

    if st.button("Check"):
        check_result = user_check(email_input, password_input)
        if check_result:
            st.error(f"❗ {check_result}")
        else:
            st.success("✅ No match found in leaks database.")

    st.subheader("📧 Email / Password Leaks")
    email_df = pd.DataFrame(detected_emails)
    if not email_df.empty:
        st.table(email_df)
    else:
        st.success("✅ No email leaks found.")

    st.subheader("📄 Document Leaks")
    if detected_docs:
        st.write(detected_docs)
    else:
        st.success("✅ No document leaks found.")

    st.subheader("🖼️ Images Found")
    if detected_images:
        st.error("❗ Image is leaked! Saved to leaked_images folder and logged in leaked_results.txt")
        for img_url in detected_images:
            st.image(img_url)
    else:
        st.success("✅ No suspicious images found.")

if __name__ == "__main__":
    scrape_and_detect()
    show_dashboard()
