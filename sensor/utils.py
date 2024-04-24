import pandas as pd
import numpy as np
import os
import logging
import json
from sensor.config import mongo_client

def dump_csv_file_to_mongodb_collection(file_path:str, database_name:str, collection_name:str) -> None:
    """
    Load a CSV file and insert its data into a MongoDB collection.

    Args:
        file_path (str): The path to the CSV file.
        database_name (str): The name of the MongoDB database.
        collection_name (str): The name of the MongoDB collection.

    Returns:
        None
    """
    try:
        # Load CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Reset DataFrame index
        df.reset_index(drop=True, inplace=True)
        
        # Convert DataFrame to JSON records
        json_records = list(json.loads(df.T.to_json()).values())
        
        # Insert JSON records into MongoDB collection
        mongo_client[database_name][collection_name].insert_many(json_records)

        # Log successful insertion
        logging.info("Data inserted into MongoDB collection successfully.")

    except Exception as e:
        # Log the exception
        logging.error(f"An error occurred: {e}")
