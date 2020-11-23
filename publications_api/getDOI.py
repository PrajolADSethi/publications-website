from habanero import Crossref
import pprint
cr = Crossref()

x = cr.works(query="Hybrid multi-objective optimization approach for neural network classification using local search")
pprint.pprint(x['message']['items'][0]["DOI"])
