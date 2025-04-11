from django.shortcuts import render,HttpResponse
from django.views import View
from accounts.models import BaseUser
from session.models import Session
# Create your views here.

from django.contrib.auth import get_user_model


class HomeView(View):
    def get(self,request,*args,**kwargs):

        # import requests
        # r = requests.get("http://index:8090/inverted_index/api/inverted_index_control/")

        context = {
        }

        return render(request,'home.html',context)

home = HomeView.as_view()
