from mainApp.models import *

def get_patient(user):

    patient= Patient.objects.get(user=user)
    return patient
def get_doctor(user):

    doctor= Doctor.objects.get(user=user)
    return doctor
    
# Check the user role after login
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

