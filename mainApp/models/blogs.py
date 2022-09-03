from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
  
    title = models.CharField(max_length=250,null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    cover_photo = models.ImageField(upload_to="blogs/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200,null=True,blank=True)


    def __str__(self):
        return self.title