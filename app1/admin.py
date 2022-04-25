from django.contrib import admin
from .models import Kitob,Muallif,Student,Record
from django.contrib.admin import ModelAdmin
from  .models import *
@admin.register(Kitob)
class KitobStudent(ModelAdmin):
    list_display = ("nom", "sahifa","janr")
    search_fields = ("id","nom",)
    list_filter = ("janr",)
    autocomplete_fields = ("muallif",)
@admin.register(Student)
class StudentAdmin(ModelAdmin):
    list_display = ("ism",)
    search_fields = ("id","ism",)

admin.site.register(Muallif)
class MuallifAdmin(ModelAdmin):
    search_fields = ("id","ism","tirik")
    autocomplete_fields = ("muallif",)
admin.site.register(Record)
# Register your models here.
