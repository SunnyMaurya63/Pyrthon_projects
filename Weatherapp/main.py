import requests
import json
import pyttsx3
city=input("Enter the name  of the city\n :")
url=f"http://api.weatherapi.com/v1/current.json?key=c8d13d4f1e904a4ca2a102800232306&q={city}"
r=requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w=wdic["current"]["temp_c"]
engine=pyttsx3.init()
engine.say(f"The temperature in {city} is {w}")
engine.runAndWait()
