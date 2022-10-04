from django.forms import ModelForm
from mainApp.models import *


class doctorProfileForm(ModelForm):
    class Meta:
        model=Doctor
        fields = ['designation','fees','bio','profile_pic','type']

class patientProfileForm(ModelForm):
    class Meta:
        model=Patient
        exclude = ['role','user','contact_no']
        