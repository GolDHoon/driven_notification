# myapp/serializers/user_serializers.py (Python)

from rest_framework import serializers
from django.contrib.auth.models import User


class SmsSendSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
