# myapp/views/user_views.py (Python)

from rest_framework import generics
from django.contrib.auth.models import User
from myapp.serializers.sms_serializers import SmsSendSerializers


class SmsSend(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = SmsSendSerializers


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = SmsSendSerializers
