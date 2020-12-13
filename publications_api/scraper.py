import scholarly_api, scopus_api, ieee_api

titles = scholarly_api.get_pubs_titles('Shilpa Sonawani')

scholarly_api.get_gs_data(titles)

scopus_api.get_scopus_data(titles)

ieee_api.get_ieee_data(titles)
