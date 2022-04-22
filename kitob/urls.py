
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', Salomlash),
    path('men/', Men),
    path('loiha/', Loiha),
    path('assosiy/', asosiy),
    path('books/', kitob),
    path(' katta_muallif/',k_muallif ),
    path('mualliflar/',mualliflar),
    path('kitob/<int:son>',kitob_delete),
    path('student/<int:son>',student),
    path('muallif/',k_muallif),








]
