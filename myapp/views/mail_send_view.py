# myapp/views/user_views.py (Python)

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from myapp.serializers.mail_serializers import MailSendSerializers


class MailSend(APIView):
    def post(self, request):
        serializer = MailSendSerializers(data=request.data)

        if serializer.is_valid():
            serializer.send()  # 이메일 발송 함수 호출
            return Response({'message': '이메일이 성공적으로 발송되었습니다.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = SmsSendSerializers
