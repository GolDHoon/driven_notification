# service/biz_msg_service.py

from datetime import datetime
from myapp.models import sms_model


def create_send_sms(validated_data):
    return sms_model.SendSMS.create(**validated_data)
