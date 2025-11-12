import pandas as pd
from src.logger import logging
from src.exception import CustomException
import os
from dataclasses import dataclass
import sys
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig


@dataclass
class DataIngestionConfig:
    train_path: str = os.path.join("artifacts","train.csv")
    test_path: str = os.path.join("artifacts","test.csv")
    raw_path: str = os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.file_path = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Intiating data ingestion")
        try:
            # provide the file path of dataset
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset")

            os.makedirs(os.path.dirname(self.file_path.raw_path),exist_ok = True)
            df.to_csv(self.file_path.raw_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            os.makedirs(os.path.dirname(self.file_path.train_path),exist_ok = True)
            train_set.to_csv(self.file_path.train_path,index=False,header=True)

            os.makedirs(os.path.dirname(self.file_path.test_path),exist_ok = True)
            test_set.to_csv(self.file_path.test_path,index=False,header=True)

            logging.info("Ingestion of the data is completed successfully!")

            return(
                self.file_path.train_path,
                self.file_path.test_path
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__ =="__main__":
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
