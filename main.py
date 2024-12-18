from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src import Logger

STAGE_NAME="Data_Ingestion_Pipeline"
try:
    Logger.info(f"<<<<<<<<<<<<<<<<<{STAGE_NAME} has been started Sucessfully..>>>>>>>>>>>>>>>>>>")
    dataingestionpipeline=DataIngestionPipeline()
    dataingestionpipeline.initiate_data_ingestion()
    Logger.info(f"<<<<<<<<<<<<<<<<<<<{STAGE_NAME} has been complated Sucessfully..>>>>>>>>>>>>>>>>>")

except Exception as e:
    raise e