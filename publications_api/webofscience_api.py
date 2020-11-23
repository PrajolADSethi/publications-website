from wos import WosClient
import wos.utils
import requests, json
import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()

token = env('WOS_TOKEN')
headers = {'Authorization': f'Token {token}', 'Content-Type': 'application/json'}
resp = requests.get("https://publons.com/api/v2/academic/publication/?academic=3714847", headers=headers)
data = json.dumps(resp.json(),
                 sort_keys=True,
                 indent=4, separators=(',', ': '))

data_dict = json.loads(data)
print(data_dict)
