from django.contrib import admin

from mainApp.models.users import Prescription

from .models import Patient,Doctor,Appointment,Faq,Testimonial,Clients
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Testimonial)
admin.site.register(Faq)
admin.site.register(Clients)

class PrescriptionAdmin(admin.ModelAdmin):
    list_display= ['__str__','get_doctor_name','get_patient_name','comment']
    readonly_fields = ('appointment',)
admin.site.register(Prescription,PrescriptionAdmin)

