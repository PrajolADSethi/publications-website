from scholarly import scholarly
import pprint
# import models


# DOCS - https://pypi.org/project/scholarly/

def get_pubs_titles(author_name):

    # Retrieve the author's data, fill-in, and print
    search_query = scholarly.search_author(author_name)
    author = next(search_query).fill()
    return ([pub.bib['title'] for pub in author.publications])

def get_gs_data(titles):

    for title in titles:


        search_query = scholarly.search_pubs(title)
        info = next(search_query)

        # ------------ ADD ALL INFO TO DB ------------
        cites = info.bib['cites']
        title = info.bib['title']
        # url = info.bib['url']
        # year = info.bib['year']
        authors = info.bib['author'] # => List of all authors
        # abstract = info.bib['abstract']
        print(f'{title}->{cites}')
    # search_query = scholarly.search_pubs()
    # author = next(search_query)
    # print(author)


# pubs_titles = get_pubs_titles('Shilpa Sonawani')
#
#
# get_gs_data(pubs_titles)

# # Retrieve the author's data, fill-in, and print
# search_query = scholarly.search_pubs('Network intrusion detection using dynamic fuzzy c means clustering')
# author = next(search_query)
# print(author.bib['author'])
#


# Print the titles of the author's publications
# print([pub.bib['title'] for pub in author.publications])


# search_query = scholarly.search_author('Shilpa Sonawani')
# print(next(search_query))
#
# # Print the titles of the author's publications
# print([pub.bib['title'] for pub in author.publications])
#
# # Take a closer look at the first publication
# pub = author.publications[0].fill()
# print(pub)
#
# # Which papers cited that publication?
# print([citation.bib['title'] for citation in pub.citedby])
