from django.contrib import admin
from .models import Teacher,Student,User

admin.site.register(User)

admin.site.register(Student)

admin.site.register(Teacher)