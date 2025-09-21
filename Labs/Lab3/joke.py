import requests

URL = "https://official-joke-api.appspot.com/random_joke"

try:
    resp = requests.get(URL, timeout=5)
    resp.raise_for_status()
    j = resp.json()
    print(j.get("setup", "No setup"))
    print(j.get("punchline", "No punchline"))
except requests.RequestException as e:
    print(f"Network/API error: {e}")
except ValueError:
    print("Invalid JSON from API.")