import requests
from bs4 import BeautifulSoup

def fetch_informatica_data():
    url = "https://www.informatica.com/products/data-security/cloud-data-masking.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = {
        "company": "Informatica",
        "use_cases": [],
        "differentiators": [],
        "market_strategy": "",
        "pricing": ""
    }
    # Example: scrape features (update as needed for real site structure)
    for li in soup.find_all("li"):
        text = li.text.strip()
        if "masking" in text.lower():
            data["use_cases"].append(text)
    return data