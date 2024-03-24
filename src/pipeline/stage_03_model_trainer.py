from src.logger import logging
from src.exception import CustomException
import os,sys
from src.entity.config_entity import ModelTrainingConfig
from src.components.model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass
    
    def inititate_model_training(self):
        try:
            model_trainer=ModelTrainer(model_trainer_config=ModelTrainingConfig())
            model_trainer.get_base_model()
            model_trainer.train_valid_generator()
            model_trainer.start_model_training()            
        except Exception as e:
            logging.exception(f"Model Training pipeline got interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        

STAGE_NAME = "Model Training"

if __name__ == "__main__":
    try:
        logging.info(f"{'>>'*10} Stage {STAGE_NAME} started {'<<'*10}")
        model_training_pipeline = ModelTrainerPipeline()
        model_training_pipeline.inititate_model_training()
        logging.info(f"{'>>'*10} Stage {STAGE_NAME} completed {'<<'*10}")
    except Exception as e:
        logging.exception(
            f"Stage {STAGE_NAME} interrupted due to {CustomException(e,sys)}"
        )
        raise CustomException(e, sys)
