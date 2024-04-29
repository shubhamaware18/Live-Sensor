from dotenv import load_dotenv
import pymongo
from sensor.constant.database import DATABASE_NAME  # Importing database constants
import certifi  # For SSL certificate verification
ca = certifi.where()  # Path to the SSL certificate store

from sensor.constant.env_variable import MONGODB_URL_KEY  # Importing MongoDB URL constant
import os
import sys
import logging

load_dotenv()  # Load environment variables from .env file

class MongoDBClient:
    """
    MongoDB client class for establishing connection and interacting with the database.
    """

    client = None  # MongoDB client instance variable

    def __init__(self, database_name=DATABASE_NAME) -> None:
        """
        Initialize MongoDB client.

        Args:
            database_name (str): Name of the MongoDB database.

        Raises:
            Exception: If an error occurs during initialization.
        """

        try:
            if MongoDBClient.client is None:  # If client not already initialized
                mongo_db_url = os.getenv(MONGODB_URL_KEY)  # Retrieve MongoDB URL from environment variables
                logging.info(f"Retrieved MongoDB URL: {mongo_db_url}")

                # Check if the URL contains "localhost", if so, connect without SSL
                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    # Connect using SSL/TLS with provided certificate
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client  # Set client instance variable
            self.database = self.client[database_name]  # Connect to specified database
            self.database_name = database_name  # Store database name

        except Exception as e:
            logging.error(f"Error initializing MongoDB client: {e}")
            raise
