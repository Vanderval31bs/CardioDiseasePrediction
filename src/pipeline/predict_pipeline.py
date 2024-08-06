import sys
import os
import pandas as pd

from src.exception import CardioPredicitonException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try: 
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)

            print("features: ", features)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)

            return preds
        
        except Exception as e:
            raise CardioPredicitonException(e, sys)


class CardioData:
    def __init__(self,
                 age: int,
                 gender: str,
                 height: float,
                 weight: float,
                 ap_hi: float,
                 ap_lo: float,
                 cholesterol: str,
                 gluc: str,
                 smoke: int,
                 alco: int,
                 active: int,
                 ):
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.ap_hi = ap_hi
        self.ap_lo = ap_lo
        self.cholesterol = cholesterol
        self.gluc = gluc
        self.smoke = smoke
        self.alco = alco
        self.active = active


    def get_data_as_frame(self):
        try:
            data = {
                'gender': [self.gender],
                'age': [self.age],
                'height': [self.height],
                'weight': [self.weight],
                'ap_hi': [self.ap_hi],
                'ap_lo': [self.ap_lo],
                'cholesterol': [self.cholesterol],
                'gluc': [self.gluc],
                'smoke': [self.smoke],
                'alco': [self.alco],
                'active': [self.active]
            }
            df = pd.DataFrame(data)
            return df
        except Exception as e:
            raise CardioPredicitonException(e, sys)
