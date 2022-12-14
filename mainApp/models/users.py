from django.db import models
from django.contrib.auth.models import User

ROLE = (
    ('patient', 'patient'),
    ('doctor', 'doctor'),
)

class Patient(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),

    )
    BLOOD = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=15,unique=True)
    father_name = models.CharField(max_length=20,null=True, blank=True)
    permanent_address = models.CharField(max_length=255,null=True,blank=True)
    ward = models.CharField(max_length=20,null=True,blank=True)
    age = models.IntegerField(null=True, blank=True)
    blood_group = models.CharField(max_length=20,choices=BLOOD,default=None,null=True, blank=True)
    nid = models.CharField(max_length=20,null=True, blank=True)

    gender = models.CharField(max_length=10,choices=GENDER, default="Male")
    role = models.CharField(max_length=10,choices=ROLE,default="patient")
    
    def __str__(self):
        return self.full_name


class Doctor(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),

    )

    TYPE = (
        ('Consultant', 'Consultant'),
        ('Telemedicine', 'Telemedicine'),
        ('Rural', 'Rural'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=15,unique=True)
    gender = models.CharField(max_length=10,choices=GENDER, default="Male")
    
    designation = models.CharField(max_length=50,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='doctor/profile_pic',null=True, blank=True)
    bio = models.TextField(max_length=255,null=True,blank=True)
    active = models.BooleanField(default=True)
    role = models.CharField(max_length=10,choices=ROLE,default="doctor")
    type = models.CharField(max_length=20,choices=TYPE,null=True, blank=True)

    facebook = models.CharField(max_length=200,null=True,blank=True)
    whatsapp = models.CharField(max_length=200,null=True,blank=True)
    fees = models.IntegerField(null=True,blank=True)
    chamber = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.full_name

class Appointment(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),

    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS,default="Pending")
    description = models.TextField(max_length=500,null=True, blank=True)
    appointment_date = models.DateField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.patient.full_name} - {self.doctor.full_name}"



class Prescription(models.Model):

    appointment = models.OneToOneField(Appointment,on_delete=models.CASCADE)
    medicines = models.CharField(max_length=255,null=True, blank=True)
    comment = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return f"{self.appointment.id} - {self.appointment.doctor.full_name}"
    
    def get_doctor_name(self):
        return f"{self.appointment.doctor.full_name}"
    def get_patient_name(self):
        return f"{self.appointment.patient.full_name}"
