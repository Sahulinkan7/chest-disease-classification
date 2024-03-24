from src.logger import logging
from src.exception import CustomException
import os,sys
from src.entity.config_entity import ModelTrainingConfig
import tensorflow as tf
from pathlib import Path

class ModelTrainer:
    def __init__(self,model_trainer_config : ModelTrainingConfig):
        try:
            
            self.model_trainer_config = model_trainer_config
            os.makedirs(self.model_trainer_config.root_dir,exist_ok=True)
            logging.info(f"Model Trainer object created")
        except Exception as e:
            logging.exception(f"Model Trainer object creation failed due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def get_base_model(self):
        try:
            logging.info(f"getting the prepared base model for model training")
            self.model:tf.keras.Model =tf.keras.models.load_model(self.model_trainer_config.updated_base_model_path)
            logging.info("prepared base model loaded successfully")
        except Exception as e:
            logging.exception(f"loading prepared base model for training got interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        try:
            model.save(path)
            logging.info(f"Trained Model saved in path : {path}")
        except Exception as e:
            raise CustomException(e, sys)
        
    def train_valid_generator(self):
        try:
            datagenerator_kwargs=dict(
                rescale=1./255,
                validation_split=0.20
            )
            
            dataflow_kwargs=dict(
                target_size=self.model_trainer_config.params_image_size[:-1],
                batch_size=self.model_trainer_config.params_batch_size,
                interpolation="bilinear"
            )
            
            valid_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
                **datagenerator_kwargs
            )
            
            logging.info(f"creating validation data generator")
            self.validation_data_generator=valid_datagenerator.flow_from_directory(
                directory=self.model_trainer_config.training_data,
                subset="validation",
                shuffle=False,
                **dataflow_kwargs
            )
            
            logging.info(f"creating training data generator")
            
            if self.model_trainer_config.params_is_augmentation:
                train_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
                    rotation_range=40,
                    horizontal_flip=True,
                    width_shift_range=0.2,
                    height_shift_range=0.2,
                    shear_range=0.2,
                    zoom_range=0.2,
                    **datagenerator_kwargs
                )
            else:
                train_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
                    **datagenerator_kwargs
                )
                
            self.training_data_generator=train_datagenerator.flow_from_directory(
                directory=self.model_trainer_config.training_data,
                subset="training",
                shuffle=True,
                **dataflow_kwargs
            )
            
            logging.info(f"Training and Validation data generator created successfully !")
            
        except Exception as e:
            logging.exception(f"Error occurred during creating validation and training data due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def start_model_training(self):
        try:
            self.steps_per_epoch = self.training_data_generator.samples//self.training_data_generator.batch_size
            self.validation_steps=self.validation_data_generator.samples//self.validation_data_generator.batch_size
            
            logging.info(f"starting model training")
            self.model.fit(self.training_data_generator,
                           epochs=self.model_trainer_config.params_epochs,
                           steps_per_epoch=self.steps_per_epoch,
                           validation_steps=self.validation_steps,
                           validation_data=self.validation_data_generator)
            logging.info(f"model training completed")
            
            self.save_model(path=self.model_trainer_config.trained_model_path,
                            model=self.model)
        except Exception as e:
            logging.exception(f"model training interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)