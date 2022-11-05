from django.contrib import admin
from .models.user import User
from .models.careTips import CareTips
from .models.diagnostic import Diagnostic
from .models.vitalSigns import VitalSigns


admin.site.register(User)
admin.site.register(CareTips)
admin.site.register(Diagnostic)
admin.site.register(VitalSigns)
# Register your models here.
