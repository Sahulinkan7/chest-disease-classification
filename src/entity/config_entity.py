from dataclasses import dataclass
from src.utils.commonutils import read_yaml
from src.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from pathlib import Path

config_file_content = read_yaml(CONFIG_FILE_PATH)
params_file_content = read_yaml(PARAMS_FILE_PATH)

@dataclass
class DataIngestionConfig:
    root_dir : Path =config_file_content['data_ingestion']['root_dir']
    source_url: str =config_file_content['data_ingestion']['source_url']
    local_data_file: Path =config_file_content['data_ingestion']['local_data_file']
    unzip_dir: Path =config_file_content['data_ingestion']['unzip_dir']
    
@dataclass
class PrepareBaseModelConfig:
    root_dir : Path = config_file_content['prepare_base_model']['root_dir']
    base_model_path: Path = config_file_content['prepare_base_model']['base_model_path']
    updated_base_model_path: Path = config_file_content['prepare_base_model']['updated_base_model_path']
    params_image_size = params_file_content["IMAGE_SIZE"]
    params_weights = params_file_content['WEIGHTS']
    params_classes = params_file_content['CLASSES']
    params_learning_rate = params_file_content['LEARNING_RATE']
    params_include_top : bool = params_file_content['INCLUDE_TOP']
    

@dataclass
class ModelTrainingConfig:
    root_dir: Path = config_file_content['training']['root_dir']
    trained_model_path: Path = config_file_content['training']['trained_model_path']
    updated_base_model_path : Path = config_file_content['prepare_base_model']['updated_base_model_path']
    training_data: Path = config_file_content['data_ingestion']['unzip_dir']
    params_epochs: int = params_file_content['EPOCHS']
    params_batch_size: int = params_file_content['BATCH_SIZE']
    params_is_augmentation: bool = params_file_content['AUGMENTATION']
    params_image_size: list = params_file_content['IMAGE_SIZE']