from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Ward)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Admission)
admin.site.register(Bed)
admin.site.register(Payment)
