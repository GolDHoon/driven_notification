# myapp/views/user_views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from myapp.models import sms_model
from myapp.serializers.sms_serializers import SmsSendSerializers
from myapp.service.sms_service import create_send_sms
from datetime import datetime
import logging
import uuid

logger = logging.getLogger(__name__)


class SmsSend(generics.ListCreateAPIView):
    queryset = sms_model.SendSMS.objects.all()
    serializer_class = SmsSendSerializers

    def post(self, request):
        # 로그 추가
        logger.debug("Received data: %s", request.data)

        request.data['CMID'] = uuid.uuid4().hex
        request.data['MSG_TYPE'] = 0
        request.data['REQUEST_TIME'] = datetime.now()
        request.data['SEND_TIME'] = datetime.now()

        # 로그 추가
        logger.debug("Modified data: %s", request.data)

        serializer = SmsSendSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            logger.info("SMS has been successfully requested.")
            return Response({'message': 'sms가 성공적으로 발송요청되었습니다.'}, status=status.HTTP_200_OK)
        else:
            logger.error("Validation errors: %s", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
