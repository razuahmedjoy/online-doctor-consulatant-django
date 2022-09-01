from django.db import models

class Gallery(models.Model):
  
    caption = models.CharField(max_length=250,null=True,blank=True)
    image = models.ImageField(upload_to="gallery/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.caption