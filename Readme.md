Data Validation Project
Overview
This project generates random weather data with intentional errors and missing values for the purpose of data validation. The generated data is then validated against specific requirements, such as missing values, unrealistic data ranges, and required columns. The cleaned data is saved to a new CSV file.

The key components of this project are:

Data Generation: Generates random weather data (temperature, humidity, precipitation, wind speed) with errors and missing values.
Data Validation: Validates the data to check for missing values, missing required columns, and unrealistic values based on given ranges.
Data Cleaning: Provides the option to clean the data by removing rows with missing values or correcting unrealistic values.
Features
Generate random weather data with errors and missing values.
Validate data to check for required columns and realistic values.
Clean data by removing rows with missing values.
Save the cleaned data to a CSV file.
Prerequisites
Ensure you have the following installed:

Python (version 3.7 or above)
Pandas: For data manipulation and handling.
Numpy: For generating random numbers and simulations.
To install the necessary libraries, run:

bash
Copy
Edit
pip install pandas numpy
Installation
Clone the repository (or download the project files):

bash
Copy
Edit
git clone https://github.com/yourusername/data-validation-project.git
Install dependencies:

Navigate to the project directory and install the required dependencies:

bash
Copy
Edit
cd data-validation-project
pip install -r requirements.txt
Configuration
config.json
This file holds configuration settings that control the behavior of the data validation and cleaning process. You can edit this file based on your data validation criteria.

required_columns: List of columns that must be present in the data.
remove_missing: Whether to remove rows with missing values.
correction: Whether to correct unrealistic values.
validation_ranges: Defines the acceptable range for certain columns (e.g., Temperature, Humidity, etc.).
cleaned_data_file: Path to save the cleaned data.
Example config.json:

json
Copy
Edit
{
    "validate": true,
    "required_columns": [
        "Location", "Date_Time", "Temperature_C", 
        "Humidity_pct", "Precipitation_mm", "Wind_Speed_kmh"
    ],
    "remove_missing": true,
    "correction": true,
    "correction_method": "removal",
    "validation_ranges": {
        "Temperature_C": { "min": -100, "max": 100 },
        "Humidity_pct": { "min": 0, "max": 100 },
        "Precipitation_mm": { "min": 0, "max": null },
        "Wind_Speed_kmh": { "min": 0, "max": null }
    },
    "cleaned_data_file": "data/data_cleaned.csv"
}
Usage
1. Data Generation
To generate random weather data with errors and missing values, run the generate_data_with_errors.py script.

bash
Copy
Edit
python generate_data_with_errors.py
This will create a file named data_with_errors.csv in the data/ directory (or another location if specified).

2. Data Validation and Cleaning
To validate and clean the data, run the main.py script.

bash
Copy
Edit
python main.py
This will:

Prompt you to enter the file path of the data file containing errors.
Allow you to specify where the cleaned data will be saved.
Run the validation process and save the cleaned data to a new CSV file.
Example
bash
Copy
Edit
Enter the path to the data file with errors: data/data_with_errors.csv
Enter the path to save cleaned data (default: data/data_cleaned.csv): data/data_cleaned.csv
After the validation and cleaning process is complete, the cleaned data will be saved to the specified output file.

Project Structure
bash
Copy
Edit
├── data/
│   ├── data_with_errors.csv           # Generated data with errors and missing values
│   └── data_cleaned.csv              # Cleaned data (after validation)
├── generate_data_with_errors.py      # Script to generate random data with errors
├── main.py                           # Main script to run validation and cleaning
├── validation.py                     # Data validation class
├── config.json                       # Configuration file for validation settings
└── README.md                         # Project documentation
Troubleshooting
Missing pandas or numpy: If you see an error indicating that pandas or numpy is missing, install them using pip install pandas numpy.
Empty Output File: If the output CSV is empty, ensure that the data file being validated has the correct structure, and the validation criteria match the data's format.
License
This project is licensed under the MIT License - see the LICENSE file for details.