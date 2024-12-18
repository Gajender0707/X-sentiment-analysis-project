from src.utils.common import make_dir,read_yaml
import requests
from src.constants import BEARER_TOKEN

import requests

url = "https://twitter-api45.p.rapidapi.com/timeline.php"

querystring = {"screenname":"elonmusk"}

headers = {
	"x-rapidapi-key": "6387b1d230msh29633aa0636c084p1aa086jsnccd798b3174e",
	"x-rapidapi-host": "twitter-api45.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())