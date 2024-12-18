from src.utils.common import make_dir,read_yaml
import requests
from src.entity.config_entity import DataIngestionConfig
from src.config.configuration import ConfigurationManager
from src import Logger
import pandas as pd
import os 
from pathlib import Path


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        make_dir(Path(self.config.row_data_path))
        
    def fetch_from_api(self):
        response=requests.get(url=self.config.api_url,
                              params=self.config.api_params,
                              headers=self.config.api_header)
        
        # Handle the response
        if response.status_code == 200:
            timeline_data = response.json()
            # print("Twitter timeline Data:", data)
        else:
            Logger.info(f"Error: {response.status_code}, Message: {response.text}")
        return timeline_data["timeline"]


    def saving_timeline_data(self):
        timeline_data=self.fetch_from_api()
        timeline_data=pd.DataFrame(timeline_data)
        timeline_data.to_csv(os.path.join(self.config.row_data_path,"timeline_data.csv"),index=False)
        Logger.info(f"Timeline data has been store to {self.config.row_data_path}")
        return timeline_data
    
    def saving_tweets_info_data(self):
        timeline_data=self.saving_timeline_data()
        tweet_id=timeline_data["tweet_id"]
        tweets_data=[]
        for i in range(len(tweet_id)):
            url = "https://twitter-api45.p.rapidapi.com/tweet.php"
            querystring = {"id":f"{tweet_id[i]}"}
            headers = {
            "x-rapidapi-key": "6387b1d230msh29633aa0636c084p1aa086jsnccd798b3174e",
            "x-rapidapi-host": "twitter-api45.p.rapidapi.com"
            }
            response2 = requests.get(url, headers=headers, params=querystring)
            data2=response2.json()
            tweets_data.append(data2)

        tweets_data=pd.DataFrame(tweets_data)
        tweets_data.to_csv(os.path.join(self.config.row_data_path,"tweets_data.csv"),index=False)
        Logger.info(f"Tweets Data has been store on  the loction {self.config.row_data_path} Sucessfully....")

        return tweets_data
                







# if __name__=="__main__":
#     data_ingestion_config=ConfigurationManager()
#     config=data_ingestion_config.get_data_ingestion_config()
#     obj=DataIngestion(config=config)
#     obj.fetch_from_api()
#     obj.saving_timeline_data()
#     obj.saving_tweets_info_data()




