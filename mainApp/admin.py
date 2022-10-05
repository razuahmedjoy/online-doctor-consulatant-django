from django.contrib import admin

from mainApp.models.users import Prescription

from .models import *
# Register your models here.
admin.site.register(Patient)

admin.site.register(Appointment)
admin.site.register(Testimonial)
admin.site.register(Faq)
admin.site.register(Clients)
admin.site.register(Gallery)
admin.site.register(HealthTeam)
admin.site.register(Village_Care_Center)
admin.site.register(Web_Settings)

admin.site.register(Slider)
admin.site.register(Counter)

admin.site.register(Blog)

class PrescriptionAdmin(admin.ModelAdmin):
    list_display= ['__str__','get_doctor_name','get_patient_name','comment']
    readonly_fields = ('appointment',)
admin.site.register(Prescription,PrescriptionAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display= ['__str__','contact_no','designation','active','role','type','fees']
    list_filter = ['type']
    list_editable = ['type','fees']

admin.site.register(Doctor,DoctorAdmin)