from django.contrib import admin
from .models import AadharModel,StudentModel

# Register your models here.
# admin.site.register(AadharModel)
# admin.site.register(StudentModel)




@admin.register(AadharModel)
class AadharAdmin(admin.ModelAdmin):
    list_display=['id','aadhar_no']

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
        list_display=['Stu_Name','aadhar_no']