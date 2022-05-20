from django.db import models
import uuid
from django.utils import timezone
from accounts.models import BaseUser

# Create your models here.

class Session(models.Model):
    class Meta:
        db_table = 'session'

    session_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    session_name = models.CharField(max_length=20)
    session_type = models.CharField(max_length=20,default='dynamic')
    is_lecture = models.BooleanField(default=False)
    #セッション公開範囲
    session_publication_range = models.CharField(max_length=20,default='all')

    session_status = models.CharField(max_length=20,default='open')
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(BaseUser,on_delete=models.CASCADE)

    session_week = models.CharField(null=True,max_length=20)
    session_time = models.CharField(null=True,max_length=20)
    session_department = models.CharField(null=True,max_length=20)
    session_subject = models.CharField(null=True,max_length=20)


class SessionComment(models.Model):
    class Meta:
        db_table = 'session_comment'

    comment_id = models.BigAutoField(primary_key=True)
    comment = models.CharField(max_length=300)
    session_id = models.ForeignKey(Session,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(BaseUser,on_delete=models.CASCADE,related_name='base_user')
    created_by_nick_name = models.CharField(max_length=20)


class SessionHistory(models.Model):
    class Meta:
        db_table = 'session_history'

    history_id = models.BigAutoField(primary_key=True)
    history_type = models.CharField(default='session_comment',max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    session_id = models.ForeignKey(Session,on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)


'''
dynamodbに最終閲覧のhistory_idを各ユーザ毎に保存しておく、次回参照はそこから行う
'''


class RegistrationSession(models.Model):
    class Meta:
        db_table = 'registration_session'

    user = models.ForeignKey(BaseUser,on_delete=models.CASCADE)
    session_id = models.ForeignKey(Session,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
