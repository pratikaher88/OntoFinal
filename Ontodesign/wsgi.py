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

list_p.append(NeuroData(patient_id = '111', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi', lab_results ='Available 23/10/2015', scan_results = 'Hip surgery history', neuro_sugery_details ='Mock Data', hospital_name='hospital1'))
list_p.append(NeuroData(patient_id = '343', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg',hospital_name='hospital1'))
list_p.append(NeuroData(patient_id = '123', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg',hospital_name='hospital1'))
list_p.append(NeuroData(patient_id = '645', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg',hospital_name='hospital1'))

NeuroData.objects.using('hospital1').bulk_create(list_p)

NeuroData.objects.using('hospital2').all().delete()

list_p = []

list_p.append(NeuroData(patient_id = '111', date ='01-01-2020', doctor_id ='222', doctors_note = 'Back next Thursday', lab_results ='Available 22/1/2016', scan_results = 'Brain damage', neuro_sugery_details ='DB2',hospital_name='hospital2'))
list_p.append(NeuroData(patient_id = '343', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg',hospital_name='hospital2'))
list_p.append(NeuroData(patient_id = '123', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg',hospital_name='hospital2'))
list_p.append(NeuroData(patient_id = '645', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg',hospital_name='hospital2'))

NeuroData.objects.using('hospital2').bulk_create(list_p)

NeuroData.objects.using('mongo').all().delete()

list_p = []

list_p.append(NeuroData(patient_id = '111', date ='01-01-2020', doctor_id ='222', doctors_note = 'Back next Thursday', lab_results ='Available 22/1/2016', scan_results = 'Brain damage', neuro_sugery_details ='DB2',hospital_name='mogodb'))
list_p.append(NeuroData(patient_id = '343', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg',hospital_name='mongodb'))
list_p.append(NeuroData(patient_id = '123', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg',hospital_name='mongodb'))
list_p.append(NeuroData(patient_id = '645', date ='01-01-2020', doctor_id ='222', doctors_note = 'loaded from wsgi is it', lab_results ='dsfs dsfg', scan_results = 'sdfsfd sdf', neuro_sugery_details ='fsd ddfg',hospital_name='mongodb'))

NeuroData.objects.using('mongo').bulk_create(list_p)


application = get_wsgi_application()
