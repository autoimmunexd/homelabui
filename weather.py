import requests
from datetime import datetime
import json  # Don't forget to import the json module

def get_weather_data():
    base_url = 'https://api.weather.gov/gridpoints/PHI/33,94/forecast'

    # Send a get request to the base_url endpoint
    response = requests.get(base_url)

    # Status code of 200 means we were successful
    if response.status_code == 200:
        # Save the info in json format to the variable data
        data = response.json()

        # Gets the properties dictionary and within that dictionary,
        # it selects the periods dictionary containing a list of dictionaries containing the data for the week.
        periods_data = data.get('properties', {}).get('periods', [])

        if periods_data:
            # Extracting values for the first hourly forecast
            first_hourly_forecast = periods_data[0]
            name_1 = first_hourly_forecast.get('name', 'N/A')
            temperature_1 = first_hourly_forecast.get('temperature', 'N/A')
            short_forecast_1 = first_hourly_forecast.get('icon', 'N/A')
            detailed_forecast_1 = first_hourly_forecast.get('detailedForecast', 'N/A')

            # Extracting values for the second hourly forecast
            second_hourly_forecast = periods_data[1]
            name_2 = second_hourly_forecast.get('name', 'N/A')
            temperature_2 = second_hourly_forecast.get('temperature', 'N/A')
            short_forecast_2 = second_hourly_forecast.get('icon', 'N/A')
            detailed_forecast_2 = second_hourly_forecast.get('detailedForecast', 'N/A')
            #print('Got the data')
            # Turns data back into a list
            ui_data = [
                {
                    "Name": name_1,
                    "Temperature": temperature_1,
                    "Detailed Forecast": detailed_forecast_1,
                    "Short Forecast": short_forecast_1
                },
                {
                    "Name": name_2,
                    "Temperature": temperature_2,
                    "Short Forecast": short_forecast_2,
                    "Detailed Forecast": detailed_forecast_2
                },
                {
                    "Updated Last": str(datetime.now().strftime("%I:%M %p"))
                 }
            ]

            # Specify the file name
            file_name = 'static/data/ui_data.json'

            # Save the data as a JSON file
            with open(file_name, 'w') as json_file:
                json.dump(ui_data, json_file, indent=2)  # indent for pretty formatting

            print(f'Data saved to {file_name}')

        else:
            print("No hourly forecast data available.")
    else:
        print("Failed to fetch weather data.")
        return None