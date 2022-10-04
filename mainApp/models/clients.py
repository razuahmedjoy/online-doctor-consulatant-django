from django.db import models

class Clients(models.Model):
    logo = models.ImageField(upload_to='clients/',null=True,blank=True)
    name = models.CharField(max_length=250,null=True,blank=True)
    url = models.URLField(max_length=200,null=True,blank=True)


    def __str__(self):
        return self.name