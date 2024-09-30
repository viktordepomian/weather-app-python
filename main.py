import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    try:
        response = requests.get(complete_url)
        
        response.raise_for_status()  

        data = response.json()
        if data['cod'] != 200:
            print(f"Error: {data['message']}")
            return

        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']
        
        print(f"\nCity: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {description.capitalize()}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    api_key = '1bce1d2e31d342aede4f167488ae07e5'  
    while True:
        city_name = input("\nEnter city name (or type 'exit' to quit): ")
        if city_name.lower() == 'exit':
            print("Exiting the weather app. Goodbye!")
            break
        get_weather(city_name, api_key)
