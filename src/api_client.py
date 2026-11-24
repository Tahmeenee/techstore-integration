import requests

BASE_URL = "https://fakestoreapi.com"


def fetch_products():
    response = requests.get(f"{BASE_URL}/products", timeout=10)
    response.raise_for_status()

    return response.json()