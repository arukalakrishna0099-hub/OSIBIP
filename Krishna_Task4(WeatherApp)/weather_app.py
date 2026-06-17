# Simple Weather App
# Oasis Infobyte Internship Project

import requests

# Enter your OpenWeatherMap API key here
API_KEY="744bac175995a605cdeca2c320588da2"

# Base URL for OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    """
    Fetch and display weather details for a given city.
    """

    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.HTTPError:
        try:
            error_data = response.json()
            print(f"\nError: {error_data.get('message', 'Unable to fetch weather data.')}")
        except ValueError:
            print("\nError: Unable to fetch weather data.")
        return

    except requests.exceptions.ConnectionError:
        print("\nError: No internet connection.")
        return

    except requests.exceptions.Timeout:
        print("\nError: Request timed out. Please try again.")
        return

    except requests.exceptions.RequestException:
        print("\nError: Something went wrong while connecting to the weather service.")
        return

    except ValueError:
        print("\nError: Invalid response received from the weather service.")
        return

    # Extract weather information
    city = data.get("name", city_name)
    country = data.get("sys", {}).get("country", "")

    main = data.get("main", {})
    weather = data.get("weather", [])
    wind = data.get("wind", {})

    temperature = main.get("temp", "N/A")
    feels_like = main.get("feels_like", "N/A")
    humidity = main.get("humidity", "N/A")
    pressure = main.get("pressure", "N/A")
    wind_speed = wind.get("speed", "N/A")

    if weather:
        description = weather[0].get("description", "N/A").title()
    else:
        description = "N/A"

    print(f"Weather Report for {city}, {country}")
    print(f" Temperature : {temperature}°C")
    print(f" Feels Like : {feels_like}°C")
    print(f" Humidity   : {humidity}%")
    print(f" Pressure   : {pressure} hPa")
    print(f" Conditions : {description}")

def main():
    print("----------SIMPLE WEATHER APP")

    if API_KEY == "YOUR_API_KEY":
        print("\nPlease add your OpenWeatherMap API key first.")
        return

    while True:
        city = input("\nEnter city name (or 'q' to quit): ").strip()

        if city.lower() == "q":
            print("\nThank you for using the Simple Weather App!")
            break

        if not city:
            print("City name cannot be empty.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()