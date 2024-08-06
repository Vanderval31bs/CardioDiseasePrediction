import os
import sys
from src.exception import CardioPredictionException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_preprocessing import DataPreprocessing
from src.components.model_trainer import ModelTrainer

@dataclass
class DataLoaderConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataLoader:
    def __init__(self):
        self.loading_config = DataLoaderConfig()

    def initiate_data_loading(self):
        logging.info("Entering the data loading method or component")
        try:
            df = pd.read_csv('notebook/data/cardio.csv', sep=";")
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.loading_config.train_data_path), exist_ok=True)

            df.to_csv(self.loading_config.raw_data_path, index=False, header=True)
            
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.loading_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.loading_config.test_data_path, index=False, header=True)
            logging.info("Loading of the data is completed")

            return (
                self.loading_config.train_data_path,
                self.loading_config.test_data_path,
            )
        except Exception as e:
            raise CardioPredictionException(e, sys)

if __name__=="__main__":
    obj = DataLoader()
    train_data, test_data = obj.initiate_data_loading()

    data_preprocessing = DataPreprocessing()
    train_arr, test_arr,_ = data_preprocessing.initiate_data_preprocessing(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))
    