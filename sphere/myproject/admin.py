from django.contrib import admin
from django.contrib.auth.models import User
from myproject.models import Professor, Course, Faculty, Comment, LikeModel
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Comment)
admin.site.register(LikeModel)
# Register your models here.
