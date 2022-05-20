from django.urls import path
from . import views

app_name = 'session'

urlpatterns = [
    path('home/',views.session_home,name='session_home'),
    path('<uuid:session_id>/top/',views.session_top,name='session_top'),
    path('create_session/',views.create_session,name='create_session'),
    path('api/session_comment/',views.session_comment_api,name='session_comment_api'),
    path('api/registration_session/',views.registration_session,name='registration_session'),
]
