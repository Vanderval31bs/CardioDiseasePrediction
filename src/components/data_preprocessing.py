import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler

from src.exception import CardioPredicitonException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataPreprocessingConfig:
    preprocessor_obj_file_path=os.path.join('artifacts', 'preprocessor.pkl')


class DataPreprocessing:
    def __init__(self):
        self.data_transformation_config = DataPreprocessingConfig()

    def drop_id_column(self, input_df):
        return input_df.drop(columns=['id'])
    
    def convert_gender_to_0_and_1(self, input_df):
        input_df['gender'] = input_df['gender'].replace({1: 0, 2: 1})
        return input_df

    def map_features_categories(self, input_df):
        level_dict = {1: 'normal', 2: 'above normal', 3: 'well above normal'}
        input_df['cholesterol'] = input_df['cholesterol'].map(level_dict)
        input_df['gluc'] = input_df['gluc'].map(level_dict)
        return input_df

    def convert_age_to_years(self, input_df):
        input_df['age'] = input_df['age'] / 365
        return input_df

    def get_formatted_df(self, input_df):
        df1 = self.drop_id_column(input_df)
        df2 = self.convert_gender_to_0_and_1(df1)
        df3 = self.map_features_categories(df2)
        df4 = self.convert_age_to_years(df3)
        return df4
    
    def get_data_transformer_object(self):
        try:
            custom_pipeline = Pipeline(
                steps=[
                    ("drop_id_column", FunctionTransformer(self.drop_id_column)),
                    ("map_features_categories", FunctionTransformer(self.map_features_categories)),
                    ("convert_age_to_years", FunctionTransformer(self.convert_age_to_years))
                ]
            )
                    
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                ]
            )

            cat_features = ["cholesterol", "gluc"]
            num_features = ["age", "gender", "height", "weight", "ap_hi", "ap_lo", "smoke", "alco", "active"]

            logging.info(f"Numerical columns: {num_features}")
            logging.info(f"Categorial columns: {cat_features}")


            feature_pipeline = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, num_features),
                    ("cat_pipeline", cat_pipeline, cat_features)
                ]
            )

            preprocessor = Pipeline(
                steps=[
                    ("custom_pipeline", custom_pipeline),
                    ("feature_pipeline", feature_pipeline)
                ],
            )

            return preprocessor
        except Exception as e:
            raise CardioPredicitonException(e, sys)
        
    def initiate_data_preprocessing(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading train and test data completed")

            logging.info("Obtaining preprocessing object")

            target_column_name="cardio"
            input_feature_train_df = train_df.drop(columns=[target_column_name])
            target_feature_train_df = train_df[target_column_name]
            
            input_feature_test_df = test_df.drop(columns=[target_column_name])
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"Applying preprocessing on training and testing dataframe")

            preprocessing_obj = self.get_data_transformer_object()

            input_feature_train_array = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_array = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_array, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_array, np.array(target_feature_test_df)]

            logging.info("Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,                
            )
            
        except Exception as e:
            raise CardioPredicitonException(e, sys)    