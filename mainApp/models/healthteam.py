from django.db import models

class HealthTeam(models.Model):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),

    )

    full_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=15,unique=True)
    gender = models.CharField(max_length=10,choices=GENDER, default="Male")
    
    profile_pic = models.ImageField(upload_to='doctor/profile_pic',null=True, blank=True)
    bio = models.TextField(max_length=255,null=True,blank=True)
    active = models.BooleanField(default=True)

    facebook = models.CharField(max_length=200,null=True,blank=True)
    whatsapp = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.full_name
