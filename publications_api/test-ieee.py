import requests
import json
import pprint

API_KEY = 'khfp46txhvhxpsd7bdjrc47c'
# scopus = Scopus(API_KEY)
#
# author = scopus.retrieve_author('24828950900')
# print(author)

resp = requests.get(f'https://ieeexploreapi.ieee.org/api/v1/search/articles?parameter&apikey={API_KEY}&article_title=Improved filter-weight algorithm for utilization-aware resource scheduling in OpenStack&author=Shilpa Sonawani'
, verify=False
)

# Further parameters' docs: https://developer.ieee.org/docs/read/Metadata_API_details

print(resp.json()['articles'][0]['citing_paper_count'])
