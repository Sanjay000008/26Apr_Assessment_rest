from django.contrib import admin
from django.urls import path,include
from restapp import views

urlpatterns = [
   path('',views.getdata),
   path('getid/<int:id>',views.getid),
   path('deletedata/<int:id>',views.deletedata),
   path('savedata/',views.savedata),
   path('updatedata/<int:id>',views.updatedata),
]