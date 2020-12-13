from pyscopus import Scopus
import requests
import json
import environ
from . import models

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

        print(resp.headers)
        data = json.dumps(resp.json(),
                         sort_keys=True,
                         indent=4, separators=(',', ': '))

        data_dict = json.loads(data)
        if 'service-error' not in data_dict:    
            if (int(data_dict['search-results']['opensearch:totalResults']) == 1):
                # ------------ ADD ALL INFO TO DB ------------
                cites = data_dict["search-results"]["entry"][0]['citedby-count']

                paper = models.Paper.objects.get(title=title)

                paper.citations_scopus = int(cites)
                paper.save()
