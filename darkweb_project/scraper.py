from bs4 import BeautifulSoup
import re
from tor_connect import tor_request

def scrape_onion_site(url):
    html = tor_request(url)
    if not html:
        return "", [], [], []

    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    passwords = re.findall(r'(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{6,}', text)
    base64_imgs = re.findall(r'data:image/\w+;base64,[A-Za-z0-9+/=]+', text)

    return text, emails, passwords, base64_imgs

if __name__ == "__main__":
    onion_url = input("Enter Onion URL: ")
    text, emails, passwords, images = scrape_onion_site(onion_url)
    print("Found Emails:", emails)
    print("Found Passwords:", passwords[:3])
    print("Found Base64 Images:", len(images))
