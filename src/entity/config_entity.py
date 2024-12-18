from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    api: dict
    row_data_path: Path
