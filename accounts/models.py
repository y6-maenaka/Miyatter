from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager
import uuid
from django.utils import timezone

class BaseUserManager(UserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('email is empty')

        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_supseruser(self,email,password):
        user = self.create_user(
            email,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class BaseUser(AbstractBaseUser,PermissionsMixin):
    class Meta:
        db_table = 'base_user'

    user_id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)

    last_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)

    nick_name = models.CharField(max_length=10,default='unknown',unique=True)

    user_type = models.CharField(default='STUDENT',max_length=20)
    authority = models.CharField(default='vw-o',max_length=20)

    objects = BaseUserManager()

    #様々な認証系で使う　一意の要素である必要があるss
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

class Student(models.Model):
    class Meta:
        db_table = 'student'

    user = models.OneToOneField(BaseUser,
                                unique=True,
                                db_index=True,
                                related_name='student',
                                on_delete=models.CASCADE)

    department = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)

class Teacher(models.Model):
    class Meta:
        db_table = 'teacher'

    user = models.OneToOneField(BaseUser,
                                unique=True,
                                related_name='teacher',
                                on_delete=models.CASCADE)

    department = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)

class Staff(models.Model):
    class Meta:
        db_table = 'staff'

    user = models.OneToOneField(BaseUser,
                                unique=True,
                                related_name='staff',
                                on_delete=models.CASCADE)


class NickName(models.Model):
    class Meta:
        db_table = 'nick_name'

    user = models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=10)
    is_using = models.BooleanField(default='false')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
