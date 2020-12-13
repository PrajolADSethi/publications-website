import requests
import json
import pprint
import environ
from . import models

env = environ.Env()
# reading .env file
environ.Env.read_env()

# Further parameters' docs: https://developer.ieee.org/docs/read/Metadata_API_details

API_KEY = env('IEEE_API_KEY')

def get_ieee_data(titles):

    for title in titles:

        resp = requests.get(f'https://ieeexploreapi.ieee.org/api/v1/search/articles?parameter&apikey={API_KEY}&article_title={title}'
            , verify=False
        )
        if resp.json()['total_records'] != 0:

            if (resp.json()['articles'][0]['title'] == title):
                # ------------ ADD ALL INFO TO DB ------------
                ieee_cites = resp.json()['articles'][0]['citing_paper_count']

                paper = models.Paper.objects.get(title=title)
                paper.citations_ieee = ieee_cites
                paper.save()
