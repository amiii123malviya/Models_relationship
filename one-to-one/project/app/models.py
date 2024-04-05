from django.db import models

# Create your models here.
class AadharModel(models.Model):
    aadhar_no=models.IntegerField()
    def __str__(self):
        return str(self.aadhar_no)

class StudentModel(models.Model):
    Stu_Name=models.CharField(max_length=100)
    Stu_Email=models.CharField(max_length=200)

    aadhar_no=models.OneToOneField(AadharModel,
    on_delete=models.PROTECT,primary_key=True)

    def __str__(self):
        return str(self.aadhar_no)