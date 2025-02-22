import os
import requests

def call_tmdb_api(url: str):
    base_url = os.getenv("TMDB_API_BASE_URL")
    secret_key = os.getenv("TMDB_API_SECRET_KEY")

    if not secret_key:
        raise ValueError("TMDB_API_SECRET_KEY environment variable is not set.")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {secret_key}",
    }

    final_url = f"{base_url}{url}"

    response = requests.get(final_url, headers=headers)
    return response.json()
