import os,sys
from src.logger import logging
from src.exception import CustomException
from pathlib import Path
import yaml

def read_yaml(file_path: Path)-> dict:
    try:
        logging.info(f"Reading yaml file from file path : {file_path}")
        with open(file_path,'r') as file:
            content = yaml.safe_load(file)
            logging.info(f"yaml file content returned")
            return content
    except Exception as e:
        logging.error(f"Reading yaml file interrupted due to the Error : {CustomException(e,sys)}")
        raise CustomException(e,sys)
    
def write_yaml(file_path : str ,content: dict) -> None:
    try:
        logging.info(f"writing yaml file in the filepath : {file_path}")
        
        if not os.path.dirname(file_path):
            logging.info(f"creating empty file {file_path}")
            with open(file_path,"w") as file:
                pass
                logging.info(f"empty file created {file_path}")
        else:
            os.makedirs(os.path.dirname(file_path),exist_ok=True)
            
        with open(file_path,"w") as file:
            logging.info(f"dumping details to yaml file {file_path}")
            yaml.dump(content,file)
            
    except Exception as e:
        logging.error(f"writing yaml file interrupted due to {CustomException(e,sys)}")
        raise CustomException(e,sys)