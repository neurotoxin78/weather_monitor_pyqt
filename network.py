#"https://api.openweathermap.org/data/2.5/onecall?lat=50.40408&lon=30.66017&exclude=current,minutely,hourly&appid=e71be9fbe7496e8dc2127b9f08afd114&units=metric&lang=ua"

import requests

class Network(object):
    """docstring for Network."""

    def __init__(self):
        self.weather_url = "https://api.openweathermap.org/data/2.5/onecall?lat=50.40408&lon=30.66017&exclude=minutely,hourly&appid=e71be9fbe7496e8dc2127b9f08afd114&units=metric&lang=ua"
        self.currency_url = "https://free.currconv.com/api/v7/convert?q=USD_UAH,EUR_UAH&compact=ultra&apiKey=824d5a4a8ff0cfb2e905"
        self.airq_url = "https://api.weatherbit.io/v2.0/current/airquality?city=kyiv&key=721c14b89aeb4edfa3efebe56722c2d7"
    def get_weather_data(self):
        return self.get_data(self.weather_url)
    def get_currency(self):
        return self.get_data(self.currency_url)
    def get_airq(self):
        return self.get_data(self.airq_url)
    def get_data(self, url):
        r = requests.get(url)
        return r.json()
