from django.db import models

class Counter(models.Model):
    title = models.CharField(max_length=100)
    count = models.IntegerField()
    image = models.ImageField(upload_to="counters/",null=True,blank=True)

    def __str__(self):
        return self.title