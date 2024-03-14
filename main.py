from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.logger import logging 
import os,sys
from src.exception import CustomException

STAGE_NAME= "Data Ingestion stage"
try:
    logging.info(f"{'>>'*10} Stage {STAGE_NAME} started {'<<'*10}")
    di= DataIngestionPipeline()
    di.initiate_data_ingestion()
    logging.info(f"{'>>'*10} Stage {STAGE_NAME} completed {'<<'*10}")
except Exception as e:
    logging.exception(f"Stage {STAGE_NAME} interrupted due to {CustomException(e,sys)}")
    raise CustomException(e,sys)


STAGE_NAME= "Prepare base model stage"
try:
    logging.info(f"{'>>'*10} Stage {STAGE_NAME} started {'<<'*10}")
    prepare= PrepareBaseModelPipeline()
    prepare.initiate_prepare_base_model()
    logging.info(f"{'>>'*10} Stage {STAGE_NAME} completed {'<<'*10}")
except Exception as e:
    logging.exception(f"Stage {STAGE_NAME} interrupted due to {CustomException(e,sys)}")
    raise CustomException(e,sys)
