import requests

api_key = "your_api_key"

while True:
    
    city = input("Enter a city name: ")

    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

    if response.status_code != 200:
        print("Sorry, the entered city name is invalid.")
    else:
        
        data = response.json()

        weather = data["weather"][0]["main"]

        if weather == "Clear":
          print("☀️" , " Clear")
        elif weather == "Clouds":
          print("☁️" , " Clouds")
        elif weather == "Rain":
          print("🌧️" , " Rain")
        elif weather == "Snow":
           print("❄️" , " Snow")
        elif weather == "Thunderstorm":
           print("⛈️" , "Thunderstrom")
        else:
         print("❓")
