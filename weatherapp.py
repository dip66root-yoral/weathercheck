import requests
import json
import pyttsx3

city = input("Enter name of the city")

url = f"https://api.weatherapi.com/v1/current.json?key=c8cbff2396644171be2113307253012&q={city}"

r = requests.get(url)

# print(r.text)
wdic = json.loads(r.text)
w =wdic["current"]["temp_c"]

text_to_speech = pyttsx3.init()
text_to_speech.say(f"'The current weather in {city} is {w} degrees'")
text_to_speech.runAndWait()

print(f"The current weather in {city} is {w} degrees")