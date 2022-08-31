from django.db import models

class Faq(models.Model):
    question = models.CharField(max_length=250,null=True,blank=True)
    answer = models.CharField(max_length=250,null=True,blank=True)


    def __str__(self):
        return self.question