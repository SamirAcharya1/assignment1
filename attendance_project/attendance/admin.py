from django.contrib import admin
from .models import Classroom, Student, Attendance

# Register your models here.
admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Attendance)