import os
import urllib.request as request
import zipfile
from mlProject.utils import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        files = [
            (self.config.source_train_URL, self.config.train_local_data_file),
            (self.config.source_test_URL, self.config.test_local_data_file)
        ]
        for url, local_path in files:
            if not os.path.exists(local_path):
                filename, headers = request.urlretrieve(
                    url = url,
                    filename = local_path
                )
                logger.info(f"{filename} download! with following info: \n{headers}")
            else:
                logger.info(f"File already exists of size: {get_size(Path(local_path))}")



    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        zip_files = [
            self.config.train_local_data_file,
            self.config.test_local_data_file
        ]

        for file in zip_files:
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
  