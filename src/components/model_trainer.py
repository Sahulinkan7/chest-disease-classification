from src.logger import logging
from src.exception import CustomException
import os,sys
from src.entity.config_entity import ModelTrainingConfig
import tensorflow as tf

class ModelTrainer:
    def __init__(self,model_trainer_config : ModelTrainingConfig):
        try:
            
            self.model_trainer_config = model_trainer_config
            os.makedirs(self.model_trainer_config.root_dir,exist_ok=True)
            logging.info(f"Model Trainer object created")
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_base_model(self):
        try:
            logging.info(f"getting the prepared base model for model training")
            self.model=tf.keras.models.load_model(self.model_trainer_config.updated_base_model_path)
            logging.info("prepared base model loaded successfully")
        except Exception as e:
            logging.exception(f"loading prepared base model for training got interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)