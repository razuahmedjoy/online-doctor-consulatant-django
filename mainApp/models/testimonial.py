from django.db import models

class Testimonial(models.Model):
    comment = models.CharField(max_length=250,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    designation = models.CharField(max_length=100,null=True,blank=True)
    photo = models.ImageField(upload_to="testimonials/")

    def __str__(self):
        return self.name