"""
WSGI config for Ontodesign project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from ontointerface.models import NeuroData


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ontodesign.settings')

NeuroData.objects.using('hospital1').all().delete()

list_p = []

list_p.append(NeuroData(patient_id = '111', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg'))
list_p.append(NeuroData(patient_id = '343', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg'))
list_p.append(NeuroData(patient_id = '123', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg'))
list_p.append(NeuroData(patient_id = '645', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg'))

NeuroData.objects.using('hospital1').bulk_create(list_p)

NeuroData.objects.using('hospital2').all().delete()

list_p = []

list_p.append(NeuroData(patient_id = '111', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='DB2'))
list_p.append(NeuroData(patient_id = '343', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg'))
list_p.append(NeuroData(patient_id = '123', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg'))
list_p.append(NeuroData(patient_id = '645', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg'))

NeuroData.objects.using('hospital2').bulk_create(list_p)


application = get_wsgi_application()
