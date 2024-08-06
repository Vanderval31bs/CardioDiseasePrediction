import os
import sys
from dataclasses import dataclass

from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score

from src.exception import CardioPredictionException
from src.logger import logging
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        self.seed = 31
    
    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Spliting training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1],
            )

            model = XGBClassifier(
                random_state=31, max_depth=4, 
                n_estimators=300, learning_rate=0.05)
            
            model.fit(X_train, y_train)
            y_train_predict = model.predict(X_train)
            train_score = accuracy_score(y_train, y_train_predict)
            
            logging.info("Achieved {train_score} accuracy on train data")            

            if (train_score < 0.6):
                raise CardioPredictionException("No best model found", sys)
            logging.info(f"Best found model on both training and testing dataset")     

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )

            y_test_predict = model.predict(X_test)
            test_accuracy = accuracy_score(y_test, y_test_predict)

            return test_accuracy



        except Exception as  e:
            raise CardioPredictionException(e, sys)