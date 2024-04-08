import requests
from datetime import datetime

# URL of the Google Sheets spreadsheet where workout data will be stored
Spreadsheet = "ADD URL"

# Get the current date and time
now = datetime.now()

# Format the current date and time into strings
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")

# Prompt the user to input the exercises they did
text = {
    "query": input("Tell me which exercises you did: ")
}

# Headers required for the API request to Nutritionix
headers = {
    'Content-Type': 'application/json',
    "x-app-id": "APP ID",
    "x-app-key": "APP KEK"
}

# Send the user's input as a query to the Nutritionix API to get information about the exercises
response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=text)
response.raise_for_status()  # Raise an exception for any HTTP error

# Extract workout data from the API response
workout = response.json()

# Loop through each exercise in the workout data
for i in range(len(workout['exercises'])):
    # Extract exercise details
    name = workout['exercises'][i]["name"]
    duration = workout['exercises'][i]["duration_min"]
    calories = workout['exercises'][i]["nf_calories"]

    # Create a dictionary containing exercise details along with date and time
    new_dict = {
        "exercise": name.title(),  # Capitalize the exercise name
        "duration": duration,
        "calories": calories,
        "date": date,
        "time": time
    }

    # Create JSON object containing the workout data
    data = {"workout": new_dict}

    # Headers required for the API request to Google Sheets
    head = {
        'Authorization': "Sheety Authentication code"
    }

    # Send a POST request to the Google Sheets spreadsheet URL with the workout data
    send = requests.post(url=Spreadsheet, json=data, headers=head)
    send.raise_for_status()  # Raise an exception for any HTTP error
