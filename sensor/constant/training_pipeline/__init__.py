import os

# Constants related to target column, pipeline, and file paths
TARGET_COLUMN = "class"  # Name of the target column in the dataset
PIPELINE_NAME = "sensor"  # Name of the pipeline
ARTIFACT_DIR = "artifact"  # Directory to store artifacts
FILE_NAME = "sensor.csv"  # Name of the main dataset file

# File names for training and testing data
TRAIN_FILE_NAME: str = "train.csv"  # Name of the training data file
TEST_FILE_NAME: str = "test.csv"  # Name of the testing data file

# File names for preprocessing and model objects, and schema file path
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"  # File name to store preprocessing object
MODEL_FILE_NAME = "model.pkl"  # File name to store trained model
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")  # Path to the schema file
SCHEMA_DROP_COLS = "drop_columns"  # Key in schema file to specify columns to drop

# Constants related to data ingestion
DATA_INGESTION_COLLECTION_NAME: str = "sensor"  # Name of the data collection
DATA_INGESTION_DIR_NAME: str = "data_ingestion"  # Directory name for data ingestion
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"  # Directory to store feature data
DATA_INGESTION_INGESTED_DIR: str = "ingested"  # Directory to store ingested data
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2  # Ratio to split data into train and test sets
