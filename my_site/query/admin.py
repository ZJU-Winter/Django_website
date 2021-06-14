from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Patientbasicinfos)
admin.site.register(models.DArearoi)
admin.site.register(models.AArearoi)
admin.site.register(models.ALabeledimage)
admin.site.register(models.Anatomydict)
admin.site.register(models.DLabeledimage)
admin.site.register(models.Diseasedict)
admin.site.register(models.HospitalRecord)
admin.site.register(models.Imagepath)
admin.site.register(models.User)
