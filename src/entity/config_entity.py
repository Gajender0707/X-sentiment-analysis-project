from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    api_url: dict
    api_header: dict
    api_params: dict
    row_data_path: Path
