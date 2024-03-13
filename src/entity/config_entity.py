from dataclasses import dataclass
from src.utils.commonutils import read_yaml
from src.constants import CONFIG_FILE_PATH
from pathlib import Path

config_file_content = read_yaml(CONFIG_FILE_PATH)

@dataclass
class DataIngestionConfig:
    root_dir : Path =config_file_content['data_ingestion']['root_dir']
    source_url: str =config_file_content['data_ingestion']['source_url']
    local_data_file: Path =config_file_content['data_ingestion']['local_data_file']
    unzip_dir: Path =config_file_content['data_ingestion']['unzip_dir']