import requests
import json


class Forecast:
    def __init__(self, city):
        self.city = city

    def weather(self):
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{self.city}/'

        params = {
            'unitGroup': 'metric',
            'key': 'MRGFY4A24UVM9DXTLLMSP2NS7',
            'contentType': 'json'
        }

        # Executing a request
        response = requests.get(url, params=params)

        # Checking whether the request was successful
        if response.status_code == 200:
            weather_data = response.json()
            weather_list = []

            # Extracting and outputting basic data
            if 'days' in weather_data:
                for day in weather_data['days']:
                    date = day.get('datetime', 'N/A')
                    temp = day.get('temp', 'N/A')
                    humidity = day.get('humidity', 'N/A')
                    wind_speed = day.get('windspeed', 'N/A')
                    conditions = day.get('conditions', 'N/A')

                    weather = (
                        f'Weather on {date} in {self.city}:'
                        f'Temperature: {temp}°C'
                        f'Humidity: {humidity}%'
                        f'Wind Speed: {wind_speed} km/h'
                        f'Conditions: {conditions}'
                        )

                    weather_list.append(weather)
                return weather_list

            else:
                print('Weather data is not available for the specified range.')

        else:
            print(f'Failed to retrieve weather data: {response.status_code}')
