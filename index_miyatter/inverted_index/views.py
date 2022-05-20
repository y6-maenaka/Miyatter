from django.shortcuts import render

from rest_framework import status,views
from rest_framework.response import Response
# Create your views here.

class InvertedIndexControlAPIViewSet(views.APIView):
    def get(self,request,*args,**kwargs):
        return Response("hello here is index",status.HTTP_200_OK)

inverted_index_control = InvertedIndexControlAPIViewSet.as_view()
