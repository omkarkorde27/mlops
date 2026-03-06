import os
from mlProject.utils import logger
from mlProject.entity.config_entity import DataValidationConfig
from pathlib import Path
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True

            for data_path, schema_key in [
                (self.config.unzip_train_data_dir, "TRAIN_COLUMNS"),
                (self.config.unzip_test_data_dir, "TEST_COLUMNS")
            ]:
                data = pd.read_csv(data_path)
                actual_cols = list(data.columns)
                expected_cols = self.config.all_schema[schema_key].keys()

                for col in actual_cols:
                    if col not in expected_cols:
                        validation_status = False
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")
                    
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e