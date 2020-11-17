from scholarly import scholarly

# DOCS - https://pypi.org/project/scholarly/

# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_pubs('Comparing openstack and vmware')
author = next(search_query)
print(author)


# Retrieve the author's data, fill-in, and print
# search_query = scholarly.search_author('Shilpa Sonawani')
# author = next(search_query).fill()
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
