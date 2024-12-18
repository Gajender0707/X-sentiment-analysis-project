from src.utils.common import make_dir,read_yaml
import requests
from src.entity.config_entity import DataIngestionConfig
from src.config.configuration import ConfigurationManager


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
    def fetch_from_api(self):
        print(self.config.api_url)
        print(self.config.api_params)
        print(self.config.api_header)
        response=requests.get(url=self.config.api_url,
                              params=self.config.api_params,
                              headers=self.config.api_header)
        
        
        # Handle the response
        if response.status_code == 200:
            data = response.json()
            print("Twitter timeline Data:", data)
        else:
            print(f"Error: {response.status_code}, Message: {response.text}")



if __name__=="__main__":
    data_ingestion_config=ConfigurationManager()
    config=data_ingestion_config.get_data_ingestion_config()
    obj=DataIngestion(config=config)
    res=obj.fetch_from_api()
    print(res)




