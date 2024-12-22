def fetch_weather_data(api_key, location, days=1):
    import requests

    # Accuweather API URL and parameters
    location_url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={location}"
    location_response = requests.get(location_url)

    if location_response.status_code == 200:
        location_data = location_response.json()
        if location_data:
            location_key = location_data[0]["Key"]
        else:
            raise Exception(f"No location data found for {location}")
    else:
        raise Exception(f"Error fetching location data: {location_response.text}")

    forecast_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/{days}day/{location_key}?apikey={api_key}"
    forecast_response = requests.get(forecast_url)

    if forecast_response.status_code == 200:
        return forecast_response.json()
    else:
        raise Exception(f"Error fetching weather data: {forecast_response.text}")


def preprocess_weather_data(data):
    processed_data = []
    for day in data["DailyForecasts"]:
        processed_data.append(
            {
                "date": day["Date"],
                "temperature_min": day["Temperature"]["Minimum"]["Value"],
                "temperature_max": day["Temperature"]["Maximum"]["Value"],
                "wind_speed": day["Day"]
                .get("Wind", {})
                .get("Speed", {})
                .get("Value", None),
                "precipitation_probability": day["Day"].get(
                    "PrecipitationProbability", None
                ),
            }
        )
    return processed_data


def get_weather_data(api_key, location, days=1):
    raw_data = fetch_weather_data(api_key, location, days)
    print(raw_data)  # Debugging: Print the raw data to inspect the structure
    return preprocess_weather_data(raw_data)
