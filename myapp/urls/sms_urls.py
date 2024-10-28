# myapp/urls/user_urls.py (Python)

from django.urls import path
from myapp.views.sms_send_view import SmsSend

urlpatterns = [
    path('send', SmsSend.as_view(), name='sms-send'),
]
