import requests
from bs4 import BeautifulSoup

def scrape_website(domain: str):

    url = f"https://{domain}"

    response = requests.get(url, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    clean_text = " ".join(text.split())

    return clean_text[:6000]