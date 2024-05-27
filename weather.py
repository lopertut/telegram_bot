import requests
import json

# Настройка параметров запроса
key = 'MRGFY4A24UVM9DXTLLMSP2NS7'
# city = input('Enter city name: ')
date1 = input('Enter start date (YYYY-MM-DD): ')
date2 = input('Enter end date (YYYY-MM-DD): ')
url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date1}/{date2}'

params = {
    'unitGroup': 'metric',
    'key': 'MRGFY4A24UVM9DXTLLMSP2NS7',
    'contentType': 'json'
}

# Выполнение запроса
response = requests.get(url, params=params)

# Проверка успешности запроса
if response.status_code == 200:
    weather_data = response.json()

    # Извлечение и вывод основных данных
    if 'days' in weather_data:
        for day in weather_data['days']:
            date = day.get('datetime', 'N/A')
            temp = day.get('temp', 'N/A')
            humidity = day.get('humidity', 'N/A')
            wind_speed = day.get('wind speed', 'N/A')
            conditions = day.get('conditions', 'N/A')

            print(f"Weather on {date} in {city}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} km/h")
            print(f"Conditions: {conditions}")
            print('---')
    else:
        print("Weather data is not available for the specified range.")

    # Пример вывода JSON ответа для просмотра структуры данных
    print(json.dumps(weather_data, indent=4))
else:
    print(f"Failed to retrieve weather data: {response.status_code}")
    weather_data = None  # Определяем переменную weather_data как None для последующего использования
