from src import Logger
from src.entity.config_entity import DataIngestionConfig
from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass


    def initiate_data_ingestion(self):
        data_ingestion_config=ConfigurationManager()
        config=data_ingestion_config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=config)
        data_ingestion.fetch_from_api()
        data_ingestion.saving_timeline_data()
        data_ingestion.saving_tweets_info_data()
        Logger.info("Data Ingestion Done Successfully.....")