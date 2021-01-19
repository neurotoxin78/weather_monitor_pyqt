#"https://api.openweathermap.org/data/2.5/onecall?lat=50.40408&lon=30.66017&exclude=current,minutely,hourly&appid=e71be9fbe7496e8dc2127b9f08afd114&units=metric&lang=ua"

import requests

class Network(object):
    """docstring for Network."""

    def __init__(self):
        self.url = "https://api.openweathermap.org/data/2.5/onecall?lat=50.40408&lon=30.66017&exclude=minutely,hourly&appid=e71be9fbe7496e8dc2127b9f08afd114&units=metric&lang=ua"
    def get_weather_data(self):
        r = requests.get(self.url)
        return r.json()
