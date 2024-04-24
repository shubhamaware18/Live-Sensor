from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection


def main():
    """
    Main function to execute the data dumping process.

    This function loads a CSV file and inserts its data into a MongoDB collection.

    Args:
        None

    Returns:
        None
    """
    try:
        # Define file path, database name, and collection name
        file_path = r"D:\Projects\Live-Sensor\aps_failure_training_set1.csv"
        database_name = "sensorpoject"
        collection_name = "livesensor"
        
        # Execute the data dumping process
        dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)
        
        # Log successful execution
        logging.info("Data dumping process completed successfully.")

    except SensorException as se:
        # Log SensorException
        logging.error(f"SensorException occurred: {se}")

    except Exception as e:
        # Log other exceptions
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
