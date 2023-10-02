from rest_framework import serializers
from .models import mydata

class MySerial(serializers.ModelSerializer):
    class Meta:
        model=mydata
        fields='__all__'