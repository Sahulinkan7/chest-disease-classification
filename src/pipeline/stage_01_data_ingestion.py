from src.logger import logging
from src.exception import CustomException
import os,sys
from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig

class DataIngestionPipeline:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            data_ingestion=DataIngestion(data_ingestion_config=DataIngestionConfig())
            data_ingestion.download_image_data()
            data_ingestion.extract_downloaded_data()
        except Exception as e:
            raise CustomException(e,sys)