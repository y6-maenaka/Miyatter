from django import forms
from .models import BaseUser,Student,Teacher,Staff
from django.contrib.auth import get_user_model

base_user = get_user_model

class LoginForm(forms.Form):
    email = forms.EmailField(
        label = 'email',
        max_length = 255,
        widget = forms.TextInput(attrs={'placeholder':'sample@gmail.com',
                                        'autoforcus':True}),
    )

    password = forms.CharField(
        label = 'password',
        strip = False,
        widget = forms.PasswordInput(attrs={'placeholder':'password'},
                                        render_value=True,
    ))

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.user_cache = None

    def clean_email(self):
        value = self.cleaned_data['email']
        return value

    def clean_password(self):
        value = self.cleaned_data['password']
        return value

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            user = get_user_model().objects.get(email=email)

        except ObjectDoesNotExist:
            raise forms.ValidationError("正しいメールアドレスを入力してください")

        if not user.check_password(password):
            raise forms.ValidationError('正しいパスワードを入力してください')

        self.user_cache = user

    def get_user(self):
        return self.user_cache

class BaseRegistrationForm(forms.ModelForm):
    class Meta:
        model = BaseUser

        fields = (
            'email',
            'password',
            'nick_name',
            'last_name',
            'first_name',
        )

    email = forms.EmailField(
        label = 'email',
        required = True,
        widget = forms.EmailInput(attrs={'placeholder':'sample@gmail.com'})
    )

    password = forms.CharField(
        label='ログインパスワード',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'ログインパスワード (例:secured-0123'}),
    )

    password2 = forms.CharField(
        label='ログインパスワード(確認用)',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'ログインパスワード(確認用)'}),
    )



class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('user',)

    department = forms.CharField(
        label = '学部',
    )

    subject = forms.CharField(
        label = '学科',
    )

class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ('user',)

class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ('user',)
