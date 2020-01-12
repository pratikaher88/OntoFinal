from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse
from .models import UserInputFormModel
from .forms import UserInputForm

from owlready2 import *


class SparqlQueries:
    def __init__(self):
        my_world = World()
        # path to the owl file is given here
        my_world.get_ontology(
            "/Users/pratikaher/ontologies/Owl-Ontology/trail.owl").load()
        sync_reasoner(my_world)  # reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()

    def search(self, query):
        resultsList = self.graph.query(query)
        return resultsList

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


def index(request):

    if request.method == 'POST':
        form = UserInputForm(request.POST)

        if form.is_valid():
            
            # Check if the user has access
            # access_result = CheckOntologyForAccess()

            # kwargs={"pid": form.cleaned_data['patient_id']}
            access_result = True

            if access_result:
                return access_granted(request,pid=1)
                # ={'product_id': 1})
            else:
                return redirect('ontointerface:access_denied')
            
            # print('Inquirer Name', form.cleaned_data['patient_id'])
    
    else:
        form = UserInputForm()

    return render(request, 'submit_access_query.html', {'form': form})


def access_denied(request):

    return render(request, 'access_denied.html')


def access_granted(request, pid):

    print("PID", pid)

    return render(request, 'access_granted.html')


