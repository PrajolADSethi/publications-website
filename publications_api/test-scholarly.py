from scholarly import scholarly

# DOCS - https://pypi.org/project/scholarly/

def get_pubs_titles(author_name):

    # Retrieve the author's data, fill-in, and print
    search_query = scholarly.search_author(author_name)
    author = next(search_query).fill()
    return ([pub.bib['title'] for pub in author.publications])

def get_gs_data(titles):

    for title in titles:
        search_query = scholarly.search_pubs(title)
        author = next(search_query)
        cites = author.bib['cites']
        title = author.bib['title']
        print(f'{title}->{cites}')
    # search_query = scholarly.search_pubs()
    # author = next(search_query)
    # print(author)
    pass

pubs_titles = get_pubs_titles('Shilpa Sonawani')
get_gs_data(pubs_titles)
# Retrieve the author's data, fill-in, and print
# search_query = scholarly.search_pubs('Comparing openstack and vmware')
# author = next(search_query)
# print(author)



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
