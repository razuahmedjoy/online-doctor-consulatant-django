
from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('profile/<int:pk>', doctor_public_profile, name='doctor_public_profile'),



    # patient dashboard
    path('patient/dashboard', patient_dashboard, name='patient_dashboard'),
    path('patient/profile', patient_profile, name='patient_profile'),
    path('patient/new_appointment', patient_new_appointment, name='patient_new_appointment'),
    path('patient/new_appointment/<int:pk>', patient_submit_new_appointment, name='patient_submit_new_appointment'),
    path('patient/appointment_details/<int:pk>', patient_appointment_details, name='patient_appointment_details'),


    # doctor dashboard
    path('doctor/dashboard', doctor_dashboard, name='doctor_dashboard'),
    path('doctor/appointment_details/<int:pk>', doctor_appointment_details, name='doctor_appointment_details'),
    path('doctor/profile', doctor_profile, name='doctor_profile'),
    path('doctor/profile/update', doctor_profile_update, name='doctor_profile_update'),


]
