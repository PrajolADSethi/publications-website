from scholarly import scholarly
import pprint
from . import models
from scholarly import ProxyGenerator
from fp.fp import FreeProxy
import time

# DOCS - https://pypi.org/project/scholarly/

def get_pubs_titles(author_name):
    # Retrieve the author's data, fill-in, and print
    search_query = scholarly.search_author(author_name)
    author = next(search_query).fill()
    # print(author.publications)
    return ([pub.bib['title'] for pub in author.publications])

def get_gs_data(author, titles):
    current_author = author

    search_query = scholarly.search_author(author)
    author = next(search_query).fill()

    for i in range(0, len(titles)):
        # ------------ ADD ALL INFO TO DB ------------
        cites = author.publications[i].bib['cites']
        title = author.publications[i].bib['title']
        # url = info.bib['url']
        year = 0
        if 'year' in author.publications[i].bib:
            year = author.publications[i].bib['year']
        else:
            year = 0
        # authors = info.bib['author'] # => List of all authors
        # abstract = info.bib['abstract']
        # if year == 'NA':
        #     year = 0

        paper = models.Paper.objects.create(
                title = title,
                co_author = current_author,
                citations_google_scholar = int(cites),
                publication_year = int(year),
                # abstract = abstract,
                # url = url,
            )
        paper.save()
        print(f'{title}->{cites}')


    # for title in titles:
    #
    #     search_query = scholarly.search_pubs(title)
    #     info = next(search_query)
    #
    #
    #
    #     print(f'{title}->{cites}')
    # search_query = scholarly.search_pubs()
    # author = next(search_query)
    # print(author)
