# myapp/serializers/user_serializers.py (Python)

from rest_framework import serializers

from myapp.models.sms_model import SendSMS


class SmsSendSerializers(serializers.ModelSerializer):
    class Meta:
        model = SendSMS
        fields = ['CMID', 'REQUEST_TIME', 'SEND_TIME', 'MSG_TYPE', 'DEST_PHONE', 'SEND_PHONE', 'MSG_BODY']