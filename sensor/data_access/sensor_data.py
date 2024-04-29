import sys
from typing import Optional

import numpy as np
import pandas as pd
import json
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.exception import SensorException

class SensorData:
    """
    A class to work with sensor data, including exporting entire MongoDB records as a pandas dataframe.
    """

    def __init__(self):
        """
        Initializes SensorData object by establishing a connection to MongoDB.
        """

        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)

        except Exception as e:
            # If an error occurs during initialization, raise SensorException
            raise SensorException(e, sys)

    def save_csv_file(self, file_path, collection_name: str, database_name: Optional[str] = None):
        """
        Saves data from a CSV file to MongoDB collection.

        Args:
            file_path (str): Path to the CSV file.
            collection_name (str): Name of the MongoDB collection.
            database_name (Optional[str]): Name of the MongoDB database. Defaults to None.

        Returns:
            int: Number of records inserted.

        Raises:
            SensorException: If an error occurs during the operation.
        """

        try:
            data_frame = pd.read_csv(file_path)  # Read data from CSV file into a pandas DataFrame
            data_frame.reset_index(drop=True, inplace=True)  # Reset DataFrame index
            records = list(json.loads(data_frame.T.to_json()).values())  # Convert DataFrame to list of records

            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            collection.insert_many(records)  # Insert records into MongoDB collection

            return len(records)  # Return the number of inserted records

        except Exception as e:
            # If an error occurs during the operation, raise SensorException
            raise SensorException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Export an entire collection from MongoDB as a pandas DataFrame.

        Args:
            collection_name (str): Name of the MongoDB collection.
            database_name (Optional[str]): Name of the MongoDB database. Defaults to None.

        Returns:
            pd.DataFrame: DataFrame containing the exported collection data.

        Raises:
            SensorException: If an error occurs during the operation.
        """

        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))  # Convert MongoDB collection to pandas DataFrame

            if "_id" in df.columns.to_list():
                df = df.drop(columns=['_id'], axis=1)  # Drop the '_id' column if present

            df.replace({"na": np.nan}, inplace=True)  # Replace 'na' with NaN

            return df  # Return the DataFrame

        except Exception as e:
            # If an error occurs during the operation, raise SensorException
            raise SensorException(e, sys)
