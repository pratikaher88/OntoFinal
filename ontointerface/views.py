from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from owlready2 import *

class SparqlQueries:
    def __init__(self):
        my_world = World()
        my_world.get_ontology("/Users/pratikaher/ontologies/Owl-Ontology/trail.owl").load() #path to the owl file is given here
        sync_reasoner(my_world)  #reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()

    def search(self,query):
        resultsList = self.graph.query(query)
        return resultsList


def index(request):

    return render(request,'display_quotes.html')

def query_output(request):

    query = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> "\
            "ask { "\
            "?isManagedBy rdfs:domain ?A ." \
            "?isManagedBy rdfs:range ?B " \
            "}"
    
    # query = "PREFIX owl: <http://www.w3.org/2002/07/owl#> "\
    #         "SELECT DISTINCT ?p "\
    #         "WHERE {?p a owl:ObjectProperty}"

    runQuery = SparqlQueries()
    response = runQuery.search(query)

    resultsList= list(response)[0]

    print(resultsList)
    

    return HttpResponse(resultsList)
