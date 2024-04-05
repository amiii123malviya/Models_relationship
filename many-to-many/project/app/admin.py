from django.contrib import admin
from .models import FuelTypeModel,CarTypeModel
# Register your models here.
# admin.site.register(FuelTypeModel)
# admin.site.register(CarTypeModel)

class Fuel(admin.ModelAdmin):
    list_display=('id','fuel_name')
admin.site.register(FuelTypeModel,Fuel)


class Car(admin.ModelAdmin):
    list_display=('id','car_name')
admin.site.register(CarTypeModel,Car)