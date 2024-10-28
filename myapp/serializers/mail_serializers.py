# myapp/serializers/user_serializers.py (Python)
from rest_framework import serializers
from myapp.service.mail_service import send_email


class MailSendSerializers(serializers.Serializer):
    receiver_email = serializers.EmailField()
    subject = serializers.CharField(max_length=255)
    body = serializers.CharField()

    def send(self):
        validated_data = self.validated_data
        send_email(
            validated_data['receiver_email'],
            validated_data['subject'],
            validated_data['body']
        )