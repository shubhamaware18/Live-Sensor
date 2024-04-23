import logging
import sys
import os
from datetime import datetime


# Define the log format
log_format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"

# Define the logger
logger = logging.getLogger("MainLogger")

# Define the log file name based on the current date and time
log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Construct the path for logs directory and the log file
logs_path = os.path.join(os.getcwd(), "logs", log_file)

# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Define the full path for the log file
log_file_path = os.path.join(logs_path, log_file)

# Configure basic logging settings
logging.basicConfig(
    filename=log_file_path,
    format=log_format,
    level=logging.INFO
)

# Log the message
logger.info("An error occurred.")
