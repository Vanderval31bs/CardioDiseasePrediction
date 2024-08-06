import logging
import os
from datetime import datetime

log_file_name = datetime.now().strftime('%m_%d_%Y_%H_%M_%S') + '.log'

logs_dir = os.path.join(os.getcwd(), "logs")
log_file_path = os.path.join(logs_dir, log_file_name)

os.makedirs(logs_dir, exist_ok=True)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO
)

# Example usage of logging
if __name__ == "__main__":
    logging.info("Logging setup complete. Log file: %s", log_file_path)
