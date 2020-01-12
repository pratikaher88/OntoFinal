from django.db import models

# Create your models here.

# class HospitalData(models.Model):

#     patient_id = models.CharField(max_length=500)


class NeuroData(models.Model):

    patient_id = models.CharField(max_length=500)
    date = models.CharField(max_length=500, blank = True)
    doctor_id = models.CharField(max_length=500, blank = True)
    doctors_note = models.CharField(max_length=500, blank = True)
    lab_results = models.CharField(max_length=500, blank = True)
    scan_results = models.CharField(max_length=500, blank = True)
    neuro_sugery_details = models.CharField(max_length=500, blank = True)

INQUIRER_CHOICES = (
    ('Admin','ADMIN'),
    ('JUNIOR NURSE', 'JUNIOR NURSE'),
    ('Surgeon','SURGEON'),
)

DATA_CHOICES = (
    ('Neuraldata','NEURODATA'),
    ('Pediatricdata', 'PEDIATRIC DATA'),
    ('Gynaecdata','Gynac Data'),
)

class UserInputFormModel(models.Model):

    patient_id = models.CharField(max_length=500)
    inquirer = models.CharField(max_length=100, choices=INQUIRER_CHOICES, default='ADMIN')
    data_requested = models.CharField(max_length=100, choices=DATA_CHOICES, default='Neuraldata')

    
    




# Patient Id	Date	Doctors Id	Doctors Note	Lab results	Scan Reports	Nuro  Surgery Details
# INDMAHMUMPARHOSA000002	8.8.19	HHHH1111NUR001	medi 6 medi 8	Test6 Negative	uploaded	NIL
# INDMAHMUMPARHOSA000002	7.7.19	HHHH1111NUR001	do test 6	NIL	NIL	NIL
# INDMAHMUMPARHOSA000002	3.4.19	HHHH1111NUR001	medi 7	NIL	NIL	NIL
# INDMAHMUMPANHOSB000005	16.5.19	HHHH1155NUR002	FGFDGFD	NIL	NIL	NIL

