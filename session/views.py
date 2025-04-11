'''========Django_views========'''
from django.shortcuts import render,HttpResponse,get_object_or_404
from django.views import View
from session.models import Session,SessionComment,RegistrationSession

# Create your views here.

class SessionHomeView(View):
    def get(self,request,*args,**kwargs):
        context = {
            "session_list":Session.objects.all(),
        }
        return render(request,'session_home.html',context)

session_home = SessionHomeView.as_view()

class SessionView(View):
    def get(self,request,*args,**kwargs):

        session_information = get_object_or_404(Session, pk=self.kwargs['session_id'])

        context = {
            'session_information':session_information,
        }

        return render(request,'session_top.html',context)

session_top = SessionView.as_view()

def create_session(request):
    if request.method == 'GET':
        return HttpResponse(200)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse('bad request')
        new_session = Session(session_name = request.POST['session_name'],created_by=request.user)
        new_session.save()
        return HttpResponse(200)


'''========DjangoRESTframework_views========'''
from rest_framework import status,views,viewsets
from rest_framework.response import Response
from .serializers import SessionCommentSerializer,RegistrationSessionSerializer
from django_filters import rest_framework as filters
from rest_framework.response import Response


class SessionCommentAPIViewSet(views.APIView):
    def get(self,request,*args,**kwargs):

        session_id = request.GET.get('session_id')
        session_comment_object = SessionComment.objects.filter(session_id = session_id)
        session_comment_serializer = SessionCommentSerializer(instance=session_comment_object,many=True)

        return Response(session_comment_serializer.data,status.HTTP_200_OK)

session_comment_api = SessionCommentAPIViewSet.as_view()

class RegistrationSessionAPIViewSet(views.APIView):
    def get(self,request,*args,**kwargs):

        registration_session_object = RegistrationSession.objects.filter(user_id = request.user.user_id)
        registration_session_serializer = RegistrationSessionSerializer(instance=registration_session_object,many=True)

        return Response(registration_session_serializer.data,status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):

        new_registration = RegistrationSessionSerializer(data=request.data)
        new_registration.is_valid(raise_exception=True)
        new_registration.save()

        return Response('hello',status.HTTP_201_CREATED)

registration_session = RegistrationSessionAPIViewSet.as_view()

