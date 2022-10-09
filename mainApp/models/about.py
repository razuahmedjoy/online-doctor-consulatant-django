from django.db import models
from django_quill.fields import QuillField

class About(models.Model):
    about_title = models.CharField(max_length=200,null=True, blank=True)
    about_top_title = models.CharField(max_length=200,null=True, blank=True)
    about_text = QuillField(null=True, blank=True)
    about_image = models.ImageField(upload_to="about/",null=True, blank=True)

    mission = QuillField(null=True, blank=True)
    phone_number = models.CharField(max_length=200,null=True, blank=True)
    email = models.CharField(max_length=200,null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)

    video_title1 = models.CharField(max_length=200,null=True, blank=True)
    video_link1 = models.CharField(max_length=250,null=True, blank=True)
    video_title2 = models.CharField(max_length=200,null=True, blank=True)
    video_link2 = models.CharField(max_length=250,null=True, blank=True)

    def __str__(self):
        return f"About Details"


class AboutTeam(models.Model):
    name= models.CharField(max_length=200,null=True, blank=True)
    designation = models.CharField(max_length=100,null=True, blank=True)
    profile_pic = models.ImageField(upload_to='about_team/',null=True, blank=True)


    def __str__(self):
        return self.name
