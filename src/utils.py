import os
import sys

import dill

from src.exception import CardioPredicitonException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CardioPredicitonException(e, sys)

def load_object(file_path):
    try: 
        with open(file_path, "rb") as file_obj:
            print("trying to load: ", file_path)
            return dill.load(file_obj)
    except Exception as e:
        print("filepath: ", file_path, " error: " , e)
        raise CardioPredicitonException(e, sys)   