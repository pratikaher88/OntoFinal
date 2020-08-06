from django.shortcuts import render, redirect
from django.urls import reverse
import requests
# Create your views here.
from django.http import HttpResponse
from .models import UserInputFormModel, NeuroData, CardioData
from .forms import UserInputForm
from Ontodesign.settings import GET_LOCATION_BY_IP, CENTER_POINT_LAT, CENTER_POINT_LONG, RADIUS
from math import radians, cos, sin, asin, sqrt
from itertools import chain

from owlready2 import *

switcher = {
    'Neuraldata': NeuroData,
    'Cardio' : CardioData
}


def location_lookup():

     r = requests.get(GET_LOCATION_BY_IP).json()
     return r['loc'].split(',')

def is_inside():

    location = location_lookup()

    center_point = [{'lat': CENTER_POINT_LAT, 'lng': CENTER_POINT_LONG}]
    test_point = [{'lat': float(location[0]), 'lng': float(location[1])}]

    lat1 = center_point[0]['lat']
    lon1 = center_point[0]['lng']
    lat2 = test_point[0]['lat']
    lon2 = test_point[0]['lng']

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 

    # print(c*r)

    if c*r <= RADIUS:
         return True
    else:
         return False


class SparqlQueries:
    def __init__(self):
        my_world = World()
        # path to the owl file is given here

        try:
            my_world.get_ontology(
                        "/Users/pratikaher/ontologies/TT2.owl").load()
        except:
            my_world.get_ontology(
                        "/Users/pratikaher/ontologies/TT2.owl").load()

        
        sync_reasoner(my_world)  # reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()

    def search(self, query):
        resultsList = self.graph.query(query)
        return resultsList

def query_output(data_requested = "Cardio", inquirer = "Inquirer"):

    # query = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> "\
    #         "ask { "\
    #         "?isManagedBy rdfs:domain ?A ." \
    #         "?isManagedBy rdfs:range ?B " \
    #         "}"
    
    # query = "PREFIX owl: <http://www.w3.org/2002/07/owl#> "\
    #         "SELECT DISTINCT ?p "\
    #         "WHERE {?p a owl:ObjectProperty}"

    print(data_requested, inquirer)
    
    query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> "\
            "PREFIX owl: <http://www.w3.org/2002/07/owl#>"\
            "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"\
            "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>"\
            "ASK{"\
            "select ?domain ?property ?range  where {"\
            "  ?property rdfs:domain ?domain ;"\
            "            rdfs:range ?range ."\
            "FILTER (regex(str(?domain), \"Inquirer\"))"\
            "FILTER (regex(str(?property), \"canAccessCardio\"))"\
            "FILTER (regex(str(?property), \"Cardio\"))"\
            "}"\
            "}"\

    print(query)

    runQuery = SparqlQueries()
    response = runQuery.search(query)

    resultsList= list(response)[0]

    # print(resultsList)

    return resultsList
    
    # return HttpResponse(resultsList)


def index(request):

    if request.method == 'POST':
        form = UserInputForm(request.POST)

        if form.is_valid():
            
            # Check if the user has access
            # access_result = CheckOntologyForAccess()

            # kwargs={"pid": form.cleaned_data['patient_id']}
            # access_result = query_output()

            pid = form.cleaned_data['patient_id']
            data_requested = form.cleaned_data['data_requested']
            inquirer = form.cleaned_data['inquirer']



            if query_output(data_requested, "Inquirer") and is_inside():
                
                return access_granted(request, pid, data_requested)
                # ={'product_id': 1})
            else:
                return redirect('ontointerface:access_denied')
            
            # print('Inquirer Name', form.cleaned_data['patient_id'])
    
    else:
        form = UserInputForm()

    return render(request, 'submit_access_query.html', {'form': form})


def access_denied(request):

    return render(request, 'access_denied.html')


def access_granted(request, pid, data_requested):

    print("PID", pid)

    print("data_requested", data_requested)

    requested_object = switcher[data_requested]
    
    # hospital1_data = requested_object.objects.filter(patient_id=pid)

    # p = requested_object('111','222','01-01-2020', 'this is it','dsfs dsfg','sdfsfd sdf','fsd ddfg')

    # p.save()

    # print(hospital1_data)
    # print(requested_object.objects.all())


    hospital1_data = requested_object.objects.using('hospital1').filter(patient_id=pid)

    hospital2_data = requested_object.objects.using('hospital2').filter(patient_id=pid)

    mongo_data = requested_object.objects.using('mongo').filter(patient_id=pid)

    # print(hospital1_data, hospital2_data)

    field_names = requested_object._meta.fields

    # # print(field_names[0].split('.')[-1])

    # total_data = hospital1_data | hospital2_data

    total_data = (list(chain(hospital1_data, hospital2_data, mongo_data)))

    print(total_data)

    return render(request, 'access_granted.html', {'hospital1_data': hospital1_data, 'hospital2_data': hospital2_data, 'mongo_data' : mongo_data, 'field_names' : field_names})

    # return render(request, 'access_granted.html', {'total_data': total_data, 'field_names' : field_names})


