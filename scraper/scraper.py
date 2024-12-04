import requests
from scraper.parser import parse_page
from scraper.config import URLS_TO_PARSE

def check_website_status(url):
    """Checking the connection status with the site."""
    try:
        response = requests.get(url, timeout=10)
        return response.status_code
    except requests.RequestException as e:
        print(f"err: Connection error with {url}: {e}")
        return None

def start_scraping(url, object_type):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"successful connection: {url}")
        # Парсинг в зависимости от типа объектов
        data = parse_page(response.text, object_type)
        return data
    else:
        print(f"err: Connection error with {url} (status code: {response.status_code})")
        return []