import os
from validation import DataValidation

def get_file_path(prompt):
    """Function to get a valid file path from the user."""
    while True:
        file_path = input(prompt)
        if not file_path:  # Check if no input is provided
            print("No input provided. Exiting...")
            exit(1)  # Exit program if no input is provided
        elif not os.path.isfile(file_path):  # Check if the file exists
            print(f"Invalid file path: {file_path}. Please try again.")
        else:
            return file_path

def get_output_file_path(default_output_file):
    """Function to get a valid output file path from the user."""
    while True:
        output_file = input(f"Enter the path to save cleaned data (default: {default_output_file}): ")
        if not output_file:  # Check if no input is provided
            return default_output_file  # Return default output file if user presses Enter
        elif not os.path.isdir(os.path.dirname(output_file)):  # Check if the directory exists
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

    try:
    # Run the validation process
        print("\nStarting the validation process...\n")
        validator.run_validation(data_file)

        print("\nData validation completed successfully!")
        print(f"Cleaned data has been saved to: {cleaned_data_file}")
    except Exception as e:
          print(f"An error occurred during validation: {e}")

if __name__ == "__main__":
    main()
