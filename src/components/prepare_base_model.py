from src.logger import logging 
from src.exception import CustomException
from src.entity.config_entity import PrepareBaseModelConfig
import os,sys
from pathlib import Path 
import tensorflow as tf

class Prepare_base_model:
    def __init__(self,prepare_base_model_config: PrepareBaseModelConfig):
        try:
            self.prepare_base_model_config = prepare_base_model_config
            os.makedirs(self.prepare_base_model_config.root_dir,exist_ok=True)
        except Exception as e:
            logging.error(f"Prepare base model object creation interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def get_base_model(self):
        try:
            logging.info(f"downloading pretrained model ")
            self.model= tf.keras.applications.vgg16.VGG16(
                input_shape=self.prepare_base_model_config.params_image_size,
                weights=self.prepare_base_model_config.params_weights,
                include_top=self.prepare_base_model_config.params_include_top
            )
            logging.info(f"Pretrained model downloaded successfully ")
            self.save_model(path=self.prepare_base_model_config.base_model_path,
                            model=self.model)
        except Exception as e:
            logging.error(f"getting base model interrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    @staticmethod
    def _prepare_full_model(model: tf.keras.Model,classes,freeze_all,freeze_till,learning_rate):
        try:
            logging.info(f"preparing the downloaded base model ")
            if freeze_all:
                for layer in model.layers:
                    model.trainable=False
            elif (freeze_till is not None) and (freeze_till>0):
                for layer in model.layers[:-freeze_till]:
                    model.trainable=False
            
            logging.info(f"flatenning the model output ")
            flatten_in = tf.keras.layers.Flatten()(model.output)
            
            logging.info(f"adding dense layer ")
            prediction = tf.keras.layers.Dense(
                units=classes,
                activation="softmax"
            )(flatten_in)
            
            logging.info(f"creating the full model ")
            full_model=tf.keras.models.Model(
                inputs=model.input,
                outputs=prediction
            )
            
            logging.info(f"compiling the model")
            full_model.compile(
                optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=['accuracy']
            )
            
            full_model.summary()
            logging.info(f"returning the fully prepared model ")
            return full_model
        
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def update_base_model(self):
        try:
            logging.info(f"starting updating the base model")
            self.full_model = self._prepare_full_model(
                model=self.model,
                classes=self.prepare_base_model_config.params_classes,
                freeze_all=True,
                freeze_till= None,
                learning_rate=self.prepare_base_model_config.params_learning_rate
            )
            
            logging.info(f"Updating the base model completed.")
            
            self.save_model(path=self.prepare_base_model_config.updated_base_model_path,
                            model=self.full_model)
        except Exception as e:
            raise CustomException(e,sys)
        
    @staticmethod
    def save_model(path:Path,model: tf.keras.Model):
        try:
            model.save(path)
            logging.info(f"Model saved in path : {path}")
        except Exception as e:
            raise CustomException(e,sys)