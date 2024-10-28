# myapp/urls/user_urls.py (Python)

from django.urls import path
from myapp.views.mail_send_view import MailSend

urlpatterns = [
    path('send', MailSend.as_view(), name='sms-send'),
]
