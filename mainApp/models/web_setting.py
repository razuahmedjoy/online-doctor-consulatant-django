from django.db import models
from django_quill.fields import QuillField

class Web_Settings(models.Model):
    medicine_bank_text = QuillField(null=True, blank=True)
    emergency_contact_text = QuillField(null=True, blank=True)
    about_title = models.CharField(max_length=200,null=True,blank=True)
    about_details = models.CharField(max_length=200,null=True,blank=True)
    menu_one = models.CharField(max_length=100,null=True, blank=True)
    menu_one_link = models.CharField(max_length=100,null=True, blank=True)
    menu_two = models.CharField(max_length=100,null=True, blank=True)
    menu_two_link = models.CharField(max_length=100,null=True, blank=True)
    menu_three = models.CharField(max_length=100,null=True, blank=True)
    menu_three_link = models.CharField(max_length=100,null=True, blank=True)
    menu_four = models.CharField(max_length=100,null=True, blank=True)
    menu_four_link = models.CharField(max_length=100,null=True, blank=True)

    scroll_notice = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return f"Settings ( Don't Delete it )"