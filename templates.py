import os
from pathlib import Path

project_name="twitter_project"

list_of_files=[
    #configuration
    f"config/config.yaml",

    #github actions
    ".github/workflows/.gitkeep",



    #Components
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/data_validation.py",
    f"src/components/model_trainer.py",
    f"src/components/model_evaluation.py",


    #Pipeline
    f"src/pipeline/__init__.py",
    f"src/pipeline/data_ingestion_pipeline.py",
    f"src/pipeline/data_transformation_pipeline.py",
    f"src/pipeline/data_validation_pipeline.py",
    f"src/pipeline/model_trainer_pipeline.py",
    f"src/pipeline/model_evaluation_pipeline.py",

    #Constants
    f"src/constants/__init__.py",

    #Entity
    f"src/entity/__init__.py",
    f"src/entity/config_entity.py",


    #utils
    f"src/utils/__init__.py",
    f"src/utils/common.py",


    #Frontent
    "templates/index.html",


    #files
    "setup.py",
    "requirements.txt",
    "main.py",
    "params.yaml",
    "schema.yaml",
    "Dockerfile",
    ".gitignore"

]




for filepath in list_of_files:
    filepath=Path(filepath)

    dirname,filename=os.path.split(filepath)
    
    if dirname !="":
        os.makedirs(dirname,exist_ok=True)



    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass