from django.contrib import admin
from .models import *


# Register your models here.
class infoData(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','title','content','created_at','updated_at']

admin.site.register(mydata,infoData)