from django.db import models

# Create your models here.
fuel=[
    ('Diesel','Diesel'),
    ('Petrol','Petrol'),
    ('CNG','CNG'),
    ('LPG','LPG'),
]

class FuelTypeModel(models.Model):
    fuel_name=models.CharField(max_length=255,choices=fuel)

    def __str__(self):
        return self.fuel_name
    
car = [
    ('Tata','Tata'),
    ('Audi','Audi'),
    ('BMW','BMW'),
    ('Toyota','Toyota'),
    ('Honda','Honda'),

]
class CarTypeModel(models.Model):
    car_name=models.CharField(max_length=255,choices=car)
    fuel_name=models.ManyToManyField(FuelTypeModel)

    def __str__(self):
        return self.car_name

    

