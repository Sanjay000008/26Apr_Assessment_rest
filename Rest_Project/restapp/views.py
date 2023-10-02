from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getdata(request):
    if request.method=='GET':
        data=mydata.objects.all()
        serial=MySerial(data,many=True)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getid(request,id):
    try:
        mid=mydata.objects.get(id=id)
    except mydata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serial=MySerial(mid)
    return Response(data=serial.data,status=status.HTTP_200_OK)
    

@api_view(['GET','DELETE'])
def deletedata(request,id):
    try:
        mid=mydata.objects.get(id=id)
    except mydata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=MySerial(mid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        mydata.delete(mid)
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        serial=MySerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
        mid=mydata.objects.get(id=id)
    except mydata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=MySerial(mid)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=MySerial(data=request.data,instance=mid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)