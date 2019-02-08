from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status 
from point_use.serializers import *
from point_use.service import *
# Create your views here.

@api_view(['POST'])
def point_use_service(request):
    print(request.data)
    tr_result = point_use(request.data)
    tr_result_serializer = TransactionSerializer(data=tr_result)
    if tr_result_serializer.is_valid(): 
        tr_result_serializer.save()
    return Response(tr_result_serializer.data, status.HTTP_200_OK)