from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from django.views import View
#ログイン周りのmod
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import LoginForm,BaseRegistrationForm,StudentRegistrationForm,TeacherRegistrationForm,StaffRegistrationForm

from django.contrib.auth import get_user_model

from .models import BaseUser,NickName

User = get_user_model()

class LoginView(View):
    def get(self,request,*args,**kwargs):

        context = {
            'login_form':LoginForm(),
        }

        return render(request,'login.html',context)

    def post(self,request,*args,**kwargs):

        login_form = LoginForm(request.POST)

        if not login_form.is_valid():
            return render(request,'login.html',{'login_form':login_form})

        user = login_form.get_user()

        auth_login(request,user)

        return redirect('accounts:login')

login = LoginView.as_view()

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        auth_logout(request)
        return redirect(reverse('home:home'))

logout = LogoutView.as_view()

class RegistrationView(View):
    def get(self,request,*args,**kwargs):

        user_type = request.GET.get('user_type')

        if(user_type == 'student'):
            registration_form = StudentRegistrationForm()

        elif(user_type == 'teacher'):
            registration_form = TeacherRegistrationForm()

        elif(user_type == 'staff'):
            registration_form = StaffRegistrationForm()

        else:
            raise ValueError('not correct format')

        context = {
            'base_registration_form':BaseRegistrationForm(),
            'each_registration_form':registration_form,
            'user_type':user_type,
        }

        return render(request,'registration.html',context)

    def post(self,request,*args,**kwargs):

        user_type = request.GET.get('user_type')


        base_registration_form = BaseRegistrationForm(request.POST,request.FILES)

        if not base_registration_form.is_valid():
            return HttpResponse('error')

        new_user = base_registration_form.save(commit=False)
        new_user.set_password(base_registration_form.cleaned_data['password'])
        new_user.is_active = True
        new_user.save()

        student_registration_form = StudentRegistrationForm(request.POST)
        if not student_registration_form.is_valid():
            return HttpResponse('error')
        new_student = student_registration_form.save(commit=False)
        new_student.user_id = new_user.user_id
        new_student.save()


        return  HttpResponse(200)


registration = RegistrationView.as_view()


class ProfileView(View):
    def get(self,request,*args,**kwargs):

        nick_name_list = NickName.objects.filter(pk=request.user.user_id)

        context = {
            "nick_name_list":nick_name_list,
        }

        return render(request,'profile.html',context)

profile = ProfileView.as_view()
