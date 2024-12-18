import os
from pathlib import Path
import yaml
from ensure import ensure_annotations
from dotmap import DotMap
from src import Logger


## Function for Creating dir
@ensure_annotations
def make_dir(dir_path: Path):
    os.makedirs(dir_path,exist_ok=True)
    Logger.info(f"directory has been created Sucessfully on location {dir_path}")


#function for reading the yaml file
@ensure_annotations
def read_yaml(filepath: Path) ->DotMap:
    with open(filepath,"r") as f:
        data=yaml.safe_load(f)
        Logger.info("Data has been load Sucessfully...")
    return DotMap(data)
