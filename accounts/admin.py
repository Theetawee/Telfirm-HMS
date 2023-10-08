from django.contrib import admin
from .models import MedicalWorker,Patient,Test,Department,Results
# Register your models here.


admin.site.register(MedicalWorker)
admin.site.register(Patient)
admin.site.register(Test)
admin.site.register(Department)
admin.site.register(Results)
