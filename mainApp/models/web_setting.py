from django.db import models
from django_quill.fields import QuillField

class Web_Settings(models.Model):
    medicine_bank_text = QuillField(null=True, blank=True)
    emergency_contact_text = QuillField(null=True, blank=True)

    def __str__(self):
        return f"Settings ( Don't Delete it )"