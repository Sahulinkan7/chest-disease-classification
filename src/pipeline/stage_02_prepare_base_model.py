from src.logger import logging
from src.exception import CustomException
import os, sys
from src.entity.config_entity import PrepareBaseModelConfig
from src.components.prepare_base_model import Prepare_base_model


class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def initiate_prepare_base_model(self):
        try:
            prepare_base_model = Prepare_base_model(
                prepare_base_model_config=PrepareBaseModelConfig()
            )
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise CustomException(e, sys)


STAGE_NAME = "Prepare Base Model"

if __name__ == "__main__":
    try:
        logging.info(f"{'>>'*10} Stage {STAGE_NAME} started {'<<'*10}")
        prepare_base_model_pipeline = PrepareBaseModelPipeline()
        prepare_base_model_pipeline.initiate_prepare_base_model()
        logging.info(f"{'>>'*10} Stage {STAGE_NAME} completed {'<<'*10}")
    except Exception as e:
        logging.exception(
            f"Stage {STAGE_NAME} interrupted due to {CustomException(e,sys)}"
        )
        raise CustomException(e, sys)
