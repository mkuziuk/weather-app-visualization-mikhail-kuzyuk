import requests

API_KEY = "7ygbsZfEPdOWA5dWaRl38yGR9JcXoLOk"


def get_location_key(city):
    url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_KEY}&q={city}"
    response = requests.get(url)
    return response.json()[0]["Key"]


def get_weather_data(location_key):
    current_conditions_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={API_KEY}"
    forecast_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location_key}?apikey={API_KEY}&metric=true"

    current_conditions = requests.get(current_conditions_url).json()
    forecast = requests.get(forecast_url).json()

    return current_conditions, forecast
