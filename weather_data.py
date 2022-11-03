"""
Pull and present 15 days of weather data for Bellingham, WA
"""

import pandas as pd
import requests


def data_pull():
    """pull 15 days of weather data from tomorrow.io"""

    url = "https://api.tomorrow.io/v4/timelines"

    location = "48.769768, -122.485886"

    querystring = {
        "location": location,
        "fields": [
            "temperature",
            "humidity",
            "windSpeed",
            "windDirection",
            "weatherCode",
        ],
        "units": "imperial",
        "timesteps": "1d",
        "apikey": "[your key goes here]",
    }

    response = requests.request("GET", url, params=querystring, timeout=10)

    return response.json()


def data_present():
    """present results of data_pull in a nice way"""

    weather_code_map = {
        0: "Unknown",
        1000: "Clear",
        1001: "Cloudy",
        1100: "Mostly Clear",
        1101: "Partly Cloudy",
        1102: "Mostly Cloudy",
        2000: "Fog",
        2100: "Light Fog",
        3000: "Light Wind",
        3001: "Wind",
        3002: "Strong Wind",
        4000: "Drizzle",
        4001: "Rain",
        4200: "Light Rain",
        4201: "Heavy Rain",
        5000: "Snow",
        5001: "Flurries",
        5100: "Light Snow",
        5101: "Heavy Snow",
        6000: "Freezing Drizzle",
        6001: "Freezing Rain",
        6200: "Light Freezing Rain",
        6201: "Heavy Freezing Rain",
        7000: "Ice Pellets",
        7101: "Heavy Ice Pellets",
        7102: "Light Ice Pellets",
        8000: "Thunderstorm",
    }

    bham_data = data_pull()

    intervals = bham_data["data"]["timelines"][0]["intervals"]

    bellingham_df = pd.DataFrame([x["values"] for x in intervals])

    bellingham_df["weatherCode"] = [
        weather_code_map[x] for x in bellingham_df["weatherCode"]
    ]

    print(bellingham_df)


def main():
    """main"""
    data_present()


if __name__ == "__main__":
    main()
