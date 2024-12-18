import os
from pathlib import Path
import yaml


## Function for Creating dir
def make_dir(dir_path: Path):
    os.makedirs(dir_path,exist_ok=True)
    print(f"directory has been created Sucessfully on location {dir_path}")


#function for reading the yaml file
def read_yaml(filepath: Path):
    with open(filepath,"r") as f:
        data=yaml.safe_load()
        print("Data read Sucessfully....")
    return data
