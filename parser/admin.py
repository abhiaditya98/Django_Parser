from django.contrib import admin
from parser import models

admin.site.register(models.Candidate)
admin.site.register(models.FileUpload)
admin.site.register(models.RequestId)
# Register your models here.
