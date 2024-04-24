from dataclasses import dataclass
import os
import pymongo

@dataclass
class EnvironmentVariable:
    """
    A data class to manage environment variables.

    Attributes:
        mongo_db_url (str): The URL of the MongoDB database.
    """
    mongo_db_url:str = os.getenv('MONGO_DB_URL')

# Instantiate EnvironmentVariable to access environment variables
env_var = EnvironmentVariable()

# Create a MongoDB client using the MongoDB database URL from environment variables
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
