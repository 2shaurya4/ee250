import os
import requests

# Prefer environment variable; fallback to placeholder
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY") or "84bb9b250f444390be354012252109"

def get_weather(city: str) -> None:
    base_url = "https://api.weatherapi.com/v1/current.json"
    params = {"key": WEATHER_API_KEY, "q": city, "aqi": "no"}

    try:
        response = requests.get(base_url, params=params, timeout=10)
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return

    if response.status_code == 200:
        try:
            data = response.json()
        except ValueError:
            print("Invalid JSON received from API.")
            return

        loc = data.get("location", {})
        cur = data.get("current", {})

        temperature_f = cur.get("temp_f")
        feels_like_f = cur.get("feelslike_f")
        condition = (cur.get("condition") or {}).get("text")
        humidity = cur.get("humidity")
        wind_speed_mph = cur.get("wind_mph")
        wind_dir = cur.get("wind_dir")
        pressure_mb = cur.get("pressure_mb")
        uv_index = cur.get("uv")
        cloud_cover = cur.get("cloud")
        visibility_miles = cur.get("vis_miles")

        city_name = loc.get("name") or city
        region = loc.get("region") or ""
        country = loc.get("country") or ""

        place = ", ".join(x for x in [city_name, region, country] if x)

        print(f"Weather data for {place}")
        print(f"Temperature: {temperature_f}°F")
        print(f"Feels Like: {feels_like_f}°F")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind_speed_mph} mph {wind_dir}")
        print(f"Pressure: {pressure_mb} mb")
        print(f"UV Index: {uv_index}")
        print(f"Cloud Cover: {cloud_cover}%")
        print(f"Visibility: {visibility_miles} miles")

    elif response.status_code in (400, 401, 402, 403, 404, 429):
        # Try to surface API's error message
        msg = ""
        try:
            msg = (response.json().get("error") or {}).get("message") or ""
        except Exception:
            pass
        messages = {
            400: "Bad Request",
            401: "Unauthorized: Invalid API key.",
            402: "Payment Required: Subscription level restriction.",
            403: "Forbidden",
            404: "Not Found: City not found.",
            429: "Too Many Requests: Rate limit exceeded.",
        }
        print(f"{messages.get(response.status_code, 'Error')} {('- ' + msg) if msg else ''}".strip())
    else:
        print(f"Error: {response.status_code}. {response.text[:200]}")

if __name__ == '__main__':
    if not WEATHER_API_KEY or WEATHER_API_KEY.startswith("<"):
        print("Set WEATHER_API_KEY environment variable to your WeatherAPI key.")
    city = input("Enter a city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("No city provided.")