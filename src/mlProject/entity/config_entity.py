from dataclasses import dataclass
from pathlib import Path

# Whenever you want to create a custom return datatype for a function you can use @dataclass to create one
# In our case we wanted get_data_ingestion_config() fn to return a custom datatype hence we made use of @dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_train_URL: str
    source_test_URL: str
    train_local_data_file: Path
    test_local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_train_data_dir: Path
    unzip_test_data_dir: Path
    all_schema: dict