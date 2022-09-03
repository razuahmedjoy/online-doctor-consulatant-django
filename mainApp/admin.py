from django.contrib import admin

from mainApp.models.users import Prescription

from .models import *
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Testimonial)
admin.site.register(Faq)
admin.site.register(Clients)
admin.site.register(Gallery)

admin.site.register(Slider)
admin.site.register(Counter)

admin.site.register(Blog)

class PrescriptionAdmin(admin.ModelAdmin):
    list_display= ['__str__','get_doctor_name','get_patient_name','comment']
    readonly_fields = ('appointment',)
admin.site.register(Prescription,PrescriptionAdmin)

