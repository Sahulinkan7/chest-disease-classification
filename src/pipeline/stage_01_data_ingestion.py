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
        
STAGE_NAME="Data Ingestion Stage"
if __name__=="__main__":
    try:
        logging.info(f"{'>>'*10} Stage {STAGE_NAME} started {'<<'*10}")
        data_ingestion_pipeline=DataIngestionPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logging.info(f"{'>>'*10} Stage {STAGE_NAME} completed {'<<'*10}")
    except Exception as e:
        logging.exception(f"")
        raise CustomException(e,sys)