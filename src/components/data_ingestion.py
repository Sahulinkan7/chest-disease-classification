from src.exception import CustomException
from src.logger import logging
import os,sys
from src.entity.config_entity import DataIngestionConfig
from pathlib import Path 
import gdown
from zipfile import ZipFile

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            os.makedirs(self.data_ingestion_config.root_dir,exist_ok=True)
        except Exception as e:
            logging.error(f"Error occurred in data ingestion object creation due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def download_image_data(self)->Path:
        try:
            data_source_url=self.data_ingestion_config.source_url
            download_dir = self.data_ingestion_config.local_data_file
            os.makedirs(os.path.dirname(download_dir))
            file_id = data_source_url.split("/")[-2]
            prefix="https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id,download_dir)
            logging.info(f"Images data downloaded into directory {download_dir}")
        except Exception as e:
            logging.error(f"Downloading data interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def extract_downloaded_data(self):
        try:
            logging.info(f"Extracting downloaded data from {self.data_ingestion_config.local_data_file}")
            extracted_data_path = self.data_ingestion_config.unzip_dir
            os.makedirs(extracted_data_path,exist_ok=True)
            with ZipFile(self.data_ingestion_config.local_data_file,'r') as zip_reference:
                zip_reference.extractall(extracted_data_path)
            logging.info(f"data extracted to {extracted_data_path}")
        except Exception as e:
            logging.error(f"Error occurred in extracting downloaded data due to {CustomException(e,sys)}")
            raise CustomException(e,sys)