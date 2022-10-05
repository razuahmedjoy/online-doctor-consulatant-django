from django.db import models
from django_quill.fields import QuillField

class Village_Care_Center(models.Model):

    full_name = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='village_care_center/profile_pic',null=True, blank=True)
    contact_no = models.CharField(max_length=15,unique=True)
    address = models.TextField(null=True, blank=True)
    details = QuillField(null=True, blank=True)

    def __str__(self):
        return self.full_name
