import scholarly_api, scopus_api, ieee_api

titles = scholarly_api.get_pubs_titles('Shilpa Sonawani')
# for each title in titles
    # create an entry in database
scholarly_api.get_gs_data(titles)

scopus_api.get_scopus_data(titles)

ieee_api.get_ieee_data(titles)
