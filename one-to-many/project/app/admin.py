from django.contrib import admin
from .models import DepartmentModel,StudentModel
# Register your models here.

# admin.site.register(StudentModel)
# admin.site.register(DepartmentModel)

@admin.register(DepartmentModel)
class Depart(admin.ModelAdmin):
    list_display=['id','dep_name']

@admin.register(StudentModel)
class Student(admin.ModelAdmin):
    list_display=['stu_name','stu_email']

