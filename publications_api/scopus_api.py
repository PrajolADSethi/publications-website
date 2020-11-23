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
def get_scopus_data(titles):

    for title in titles:

        resp = requests.get(f"http://api.elsevier.com/content/search/scopus?query=TITLE({title})&field=citedby-count",
                            headers={'Accept':'application/json',
                                     'X-ELS-APIKey': API_KEY})
        data = json.dumps(resp.json(),
                         sort_keys=True,
                         indent=4, separators=(',', ': '))

        data_dict = json.loads(data)
        if (int(data_dict['search-results']['opensearch:totalResults']) == 1):
            # ------------ ADD ALL INFO TO DB ------------
            ieee_cites = data_dict["search-results"]["entry"][0]

# resp2 = requests.get("http://api.elsevier.com/content/search/scopus?query=AU-ID(36706629400)?field=authors,title",
#                     headers={'Accept':'application/json',
#                              'X-ELS-APIKey': API_KEY})
#
# results = resp2.json()
# print(results)
resp = requests.get(f"http://api.elsevier.com/content/search/scopus?query=TITLE(Not a valid title)&field=citedby-count",
                    headers={'Accept':'application/json',
                             'X-ELS-APIKey': API_KEY})
data = json.dumps(resp.json(),
                 sort_keys=True,
                 indent=4, separators=(',', ': '))

data_dict = json.loads(data)
print()
