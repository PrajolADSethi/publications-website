from pyscopus import Scopus
import requests
import json
import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()
# API Docs - https://kitchingroup.cheme.cmu.edu/blog/2015/04/03/Getting-data-from-the-Scopus-API/

API_KEY = env('SCOPUS_API_KEY')
scopus = Scopus(API_KEY)

# author = scopus.retrieve_author('36706629400')
# print(author)

resp = requests.get("http://api.elsevier.com/content/search/scopus?query=TITLE(Improved Logistic Regression Approach in Feature Selection for EHR)&field=citedby-count",
                    headers={'Accept':'application/json',
                             'X-ELS-APIKey': API_KEY})
data = json.dumps(resp.json(),
                 sort_keys=True,
                 indent=4, separators=(',', ': '))

data_dict = json.loads(data)
print(data_dict["search-results"]["entry"][0])

# resp2 = requests.get("http://api.elsevier.com/content/search/scopus?query=AU-ID(36706629400)?field=authors,title",
#                     headers={'Accept':'application/json',
#                              'X-ELS-APIKey': API_KEY})
#
# results = resp2.json()
# print(results)
