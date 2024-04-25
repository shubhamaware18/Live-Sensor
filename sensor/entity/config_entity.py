from datetime import datetime  # Import datetime module to work with timestamps
from sensor.constant import training_pipeline  # Import constants related to the training pipeline
import os
import sys

# Class for Training Pipeline config
class TrainingPipelineConfig:
    """
    Configuration class for the training pipeline.
    """

    def __init__(self, timestamp: datetime = datetime.now()):
        """
        Initializes the TrainingPipelineConfig object.

        Args:
            timestamp (datetime, optional): Timestamp for the current configuration. Defaults to current datetime.
        """
        
        try:
            timestamp = timestamp.strftime("%m_%d_%Y_%M_%S")

            self.pipeline_name = training_pipeline.PIPELINE_NAME  # Name of the training pipeline

            # Directory to store artifacts, including timestamp for versioning
            self.artifact_dir = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)

            self.timestamp: str = timestamp  # Timestamp as a string
        
        except Exception as e:
            print(f"An error occurred while initializing TrainingPipelineConfig: {e}")
            sys.exit(1)


# Class for Data Ingestion config
class DataIngestionConfig:
    """
    Configuration class for data ingestion.
    """

    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        """
        Initializes the DataIngestionConfig object.

        Args:
            training_pipeline_config (TrainingPipelineConfig): Configuration object for the training pipeline.
        """
        
        try:
            # Directory for data ingestion within the artifact directory
            self.data_ingestion_dir = os.path.join(
                training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME
            )

            # File path for the feature store
            self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
            )

            # File path for the training data
            self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
            )

            # File path for the testing data
            self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
            )

            # Ratio to split data into train and test sets
            self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO

            # Name of the data collection
            self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        
        except Exception as e:
            print(f"An error occurred while initializing DataIngestionConfig: {e}")
            sys.exit(1)
