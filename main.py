import os
from validation import DataValidation

def get_file_path(prompt):
    """Function to get a valid file path from the user."""
    while True:
        file_path = input(prompt)
        if os.path.isfile(file_path):  # Check if the file exists
            return file_path
        else:
            print(f"Invalid file path: {file_path}. Please try again.")

def get_output_file_path(default_output_file):
    """Function to get a valid output file path from the user."""
    while True:
        output_file = input(f"Enter the path to save cleaned data (default: {default_output_file}): ")
        if not output_file:
            return default_output_file  # Return default output file if user presses Enter
        elif not os.path.isdir(os.path.dirname(output_file)):
            print(f"Invalid directory: {os.path.dirname(output_file)}. Please try again.")
        else:
            return output_file

def main():
    # Greeting message for the user
    print("Welcome to the Data Validation Script!")

    # Initialize the DataValidation class with the config file
    validator = DataValidation()

    # Get the file path for the data with errors
    data_file = get_file_path("Enter the path to the data file with errors: ")

    # Get the output file path where cleaned data will be saved
    cleaned_data_file = get_output_file_path(r"data/data_cleaned.csv")  # Default output path

    # Update the config with the user-defined output file path
    validator.config["cleaned_data_file"] = cleaned_data_file

    # Run the validation process
    print("\nStarting the validation process...\n")
    validator.run_validation(data_file)

    print("\nData validation completed successfully!")
    print(f"Cleaned data has been saved to: {cleaned_data_file}")

if __name__ == "__main__":
    main()
