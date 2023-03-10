# any excetion that happens that can be logged to we can track - ex say we have error it is tracked

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # will create a text will with naming convetion of month year day hour..
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) # logs folder created in same folder then all the file created will start with logs followed by LOG_FILE
os.makedirs(logs_path,exist_ok = True) # if file exists append in it is the use of exits_ok

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)