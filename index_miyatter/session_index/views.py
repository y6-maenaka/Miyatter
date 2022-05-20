from django.shortcuts import render

from rest_framework import status,views
from rest_framework.response import Response
# Create your views here.


class SessionIndexAPIViewSet(views.APIView):
    def get(self,request,*args,**kwargs):
        return Response('ok',status.HTTP_200_OK)

session_index = SessionIndexAPIViewSet.as_view()
