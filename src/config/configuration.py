from src.constants import CONFIG_YAML_PATH
from src.utils.common import make_dir,read_yaml
from pathlib import Path
from src.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    
    def __init__(self,config_yaml_path=CONFIG_YAML_PATH):
        self.config=read_yaml(Path(config_yaml_path))


    #initiate DataIngestionConfiguation
    def get_data_ingestion_config(self) ->DataIngestionConfig:
        data_ingestion_info=self.config.DataIngestionConfig

        api_url=data_ingestion_info.api.url
        api_header={
            "x-rapidapi-key":data_ingestion_info.api.x_rapidapi_key,
            "x-rapidapi-host":data_ingestion_info.api.x_rapidapi_host
        }
        api_params={
            "screenname":data_ingestion_info.api.screenname
        }
        data_ingestion_config=DataIngestionConfig(
            api_url=api_url,
            api_header=api_header,
            api_params=api_params,
            row_data_path=data_ingestion_info.row_data_path
        )
        return data_ingestion_config




if __name__=="__main__":
    obj=ConfigurationManager()
    res=obj.get_data_ingestion_config()
    print(res)
    