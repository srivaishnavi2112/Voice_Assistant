import requests
from secret import *
api_address='http://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid='+key2
json_data=requests.get(api_address).json()
def temp():
    t=round(json_data["main"]["temp"]-273,1)
    return t
def des():
    desc=json_data["weather"][0]["description"]
    return desc
