## Workout_Logger_using_Nutritionix_API_and_Google-Sheets


This script allows users to log their workout data, including exercise name, duration, calories burned, date, and time, into a Google Sheets spreadsheet. The workout data is obtained by querying the Nutritionix API based on the exercises input by the user.

**Features:**

- Prompt users to input the exercises they did.
- Send the user's input as a query to the Nutritionix API to retrieve exercise details.
- Extract workout data from the API response, including exercise name, duration, and calories burned.
- Format the workout data along with the current date and time.
- Send the formatted data to a Google Sheets spreadsheet for logging.

**Setup:**

1. Obtain Nutritionix API credentials:
   - Sign up for a Nutritionix developer account to get API access.
   - Obtain the `x-app-id` and `x-app-key` required for making requests to the Nutritionix API.

2. Create a Google Sheets spreadsheet:
   - Create a new Google Sheets spreadsheet where the workout data will be logged.

3. Set up Google Sheets API access:
   - Enable the Google Sheets API for your Google Cloud project.
   - Create OAuth credentials (service account or OAuth client ID) with sufficient permissions to write to the Google Sheets spreadsheet.

4. Obtain Google Sheets API credentials:
   - Download the credentials JSON file containing your service account credentials or OAuth client ID and secret.

5. Add dependencies:
   - Install the `requests` library using pip: `pip install requests`.

**Usage:**

1. Replace placeholders in the script:
   - Replace the `Spreadsheet` variable with the URL of your Google Sheets spreadsheet.
   - Replace the `x-app-id` and `x-app-key` variables with your Nutritionix API credentials.
   - Replace the `'Authorization'` header value with your Google Sheets API authentication code or token.

2. Run the script:
   - Execute the script in a Python environment: `python workout_logger.py`.
   - Follow the prompts to input the exercises you did.

**Contributing:**

Contributions to enhance the functionality, improve error handling, or add new features are welcome. Please fork the repository, make your changes, and submit a pull request with a clear description of the proposed changes.

**Acknowledgments:**

- This project utilizes the Nutritionix API to retrieve exercise data.
- It leverages the Google Sheets API for logging workout data into a Google Sheets spreadsheet.

## Author

[Esrael Mekdem](https://github.com/Ezzy401k)