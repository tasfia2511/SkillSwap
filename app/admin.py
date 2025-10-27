from django.contrib import admin

# Register your models here.
from .models import Skill, CanTeach, CanLearn

admin.site.register(Skill)
admin.site.register(CanTeach)
admin.site.register(CanLearn)
