import pandas as pd
import json
import os

class DataValidation:
    def __init__(self, config_file=r"config.json"):
        """Load configuration from the provided JSON file."""
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        """Load configuration from a JSON file."""
        with open(config_file, "r") as file:
            return json.load(file)

    def validate_data(self, df):
        """Validate data based on the loaded configuration."""
        print("Starting data validation...")

        # Check for missing columns
        required_columns = self.config.get("required_columns", [])
        if not all(col in df.columns for col in required_columns):
            print(f"Error: Missing required columns. Expected columns: {required_columns}")
            return None

        # Handle missing values if specified in the config
        if self.config.get("remove_missing", False):
            print("Removing rows with missing values.")
            df = df.dropna()

        # Handle unrealistic values based on config validation ranges
        validation_ranges = self.config.get("validation_ranges", {})
        for column, range_info in validation_ranges.items():
            if column in df.columns:
                min_value = range_info.get("min", -float("inf"))
                max_value = range_info.get("max", float("inf"))

                # Treat max value 'null' as a very large value
                if max_value is None:
                    max_value = float("inf")

                # Apply range validation
                df = df[(df[column] >= min_value) & (df[column] <= max_value)]
        
        # Handle corrections if specified
        if self.config.get("correction", False):
            correction_method = self.config.get("correction_method", "removal")
            if correction_method == "removal":
                # Remove rows that don't fit within the validation ranges
                df = df.dropna(subset=validation_ranges.keys())

        # Return the cleaned dataframe
        return df

    def save_cleaned_data(self, df):
        """Save the cleaned data to a new CSV file."""
        cleaned_data_file = self.config.get("cleaned_data_file", r"data/data_cleaned.csv")

        # Ensure the directory exists
        directory = os.path.dirname(cleaned_data_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory {directory} created.")

        try:
            # Save cleaned data to CSV
            df.to_csv(cleaned_data_file, index=False)
            print(f"Cleaned data saved to {cleaned_data_file}")
        except Exception as e:
            print(f"Error saving cleaned data: {e}")

        print("Data validation completed.")

    def run_validation(self, data_file):
        """Load data, and perform validation."""
        # Load the generated data
        try:
            df = pd.read_csv(data_file)
            print("Data loaded successfully.")
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

        # Perform data validation and get cleaned data
        cleaned_df = self.validate_data(df)

        if cleaned_df is not None:
            # Save the cleaned data
            self.save_cleaned_data(cleaned_df)

        print("The dataset is valid and ready for use.")
