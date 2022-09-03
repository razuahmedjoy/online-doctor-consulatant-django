from django.db import models

class Slider(models.Model):
    image = models.ImageField(upload_to='slider/')
    title = models.CharField(max_length=100,null=True,blank=True)
    caption = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(max_length=500)


    def __str__(self):
        return self.title