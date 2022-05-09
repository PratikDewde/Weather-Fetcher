import requests

API_KEY = "10679a0adac7434cdd6a971994a53ce1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a City name : ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"]-273.15,2)

    print("weather:",weather)
    print("temperature",temperature,"celsius")

else:
    print("AN error occured.")