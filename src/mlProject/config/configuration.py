from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import DataIngestionConfig, DataValidationConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_train_URL=config.source_train_URL,
            source_test_URL=config.source_test_URL,
            train_local_data_file=config.train_local_data_file,
            test_local_data_file=config.test_local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        train_schema = self.schema.TRAIN_COLUMNS
        test_schema = self.schema.TEST_COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,  # Need to fix this part
            STATUS_FILE= config.STATUS_FILE,
            unzip_train_data_dir = config.unzip_train_data_dir,
            unzip_test_data_dir = config.unzip_test_data_dir,
            all_schema = {"TRAIN_COLUMNS": train_schema, "TEST_COLUMNS": test_schema},
        )

        return data_validation_config