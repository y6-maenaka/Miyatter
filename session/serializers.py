from rest_framework import serializers
from .models import SessionComment,Session, RegistrationSession
from accounts.models import BaseUser


class SessionCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = SessionComment
        fields = ['comment_id','comment','session_id','created_at','created_by_nick_name']


class RegistrationSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistrationSession
        fields = ['user','session_id','created_at']
