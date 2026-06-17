#simple weather app
#oasis infobyte Internship project
import requests

API_KEY = "744bac175995a605cdeca2c320588da2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    
    """
    fetch and display weather  details for a city 
    """
    params={
        "q": city_name,
        "appid": API_KEY,
        "units": "metric" # to get temperature in celsius
    }

    try:
        response = requests.get(BASE_URL, params=params,timeout=5)
        data= response.json()
    except requests.exceptions.RequestException :
        print("Error: Unable to connect to the weather service.")
        return
    
#API sends a code like 200(success) ,404 (city not found). etc .
    code=str(data.get("cod",""))


    if code != "200":
        #show error message from the API if available
        message=data.get("message","Unknown error occurred.")
        print(f"Error from weather service: {message}")
        return
    # extract main weather deatils 
    main_data=data.get("main",{})
    weather_list=data.get("weather",[])

    temp=main_data.get("temp" ,"N/A")
    feels_like=main_data.get("feels_like", "N/A")
    humidity=main_data.get("humidity", "N/A")

    if weather_list:
        description=weather_list[0].get("description","N/A")
    else:
        description="N/A"

    #print the results
    print(f"\nWeather in {city_name.title()}:")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"conditions: {description}")

def main():
    print("------Simple Weather App------")
    
    if API_KEY == "your_API_KEY_HERE":
        print("please set your OpenWeatherMap API key in the API_KEY variable first.")
        return
    city=input("Enter the city name:").strip()
    
    if city == "":
        print("city name cannot be empty.")
        return
    
    get_weather(city)
    print("\nThank you for using the Simple weather app.")
    print("-------End of Program------")

if __name__ == "__main__":
    main()
