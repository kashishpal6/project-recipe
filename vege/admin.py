from django.contrib import admin
from .models import*
admin.site.register(Recipe)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)

admin.site.register(Subject)
admin.site.register(SubjectMarks)