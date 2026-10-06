import requests
import sys


def get_coordinates(city):
    response = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1},
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()

    if "results" not in data:
        raise ValueError(f"City not found: {city}")
    place = data["results"][0]
    return place["latitude"], place["longitude"], place["name"], place["country"]


def get_current_weather(latitude, longitude):
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m",
        },
        timeout=10,
    )

    response.raise_for_status()
    data = response.json()
    current = data["current"]
    return current["temperature_2m"], current["wind_speed_10m"]


def main():
    city = input("City: ").strip()
    if not city:
        sys.exit("Error: You must enter a city")
    try:
        latitude, longitude, name, country = get_coordinates(city)
        temperature, wind = get_current_weather(latitude, longitude)
    except ValueError as error:
        sys.exit(f"Error: {error}")
    except requests.exceptions.RequestException:
        sys.exit("Error: Could not connect to the weather service. Check your internet connection.")
    print(f"{name}, {country}: {temperature}°C, wind {wind}km/h")


if __name__ == "__main__":
    main()
