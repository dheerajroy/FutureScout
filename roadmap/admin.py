from django.contrib import admin
from .models import Exam, Course, EducationEstablishment, RoadMap

admin.site.site_header = admin.site.site_title = 'Future Scout Admin Panel'
admin.site.index_title = 'Welcome To ' + admin.site.site_header

admin.site.register(Exam)
admin.site.register(Course)
admin.site.register(EducationEstablishment)
admin.site.register(RoadMap)
