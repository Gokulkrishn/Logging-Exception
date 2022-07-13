from genericpath import exists
import logging
import os
from datetime import datetime

LOG_DIR='logs'
os.makedirs(LOG_DIR,exist_ok=True)

CURRENT_TIME_STAMP = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)


logging.basicConfig(filename=LOG_FILE_PATH,
                    filemode='w',
                    format='[%(asctime)s] %(name)s -%(levelname)s - %(message)s',
                    level=logging.INFO
)                    
