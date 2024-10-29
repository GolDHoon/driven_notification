# models.py

from django.db import models

class SendSMS(models.Model):
    MSG_TYPE = models.IntegerField()
    CMID = models.CharField(max_length=32)
    REQUEST_TIME = models.DateTimeField()
    SEND_TIME = models.DateTimeField()
    DEST_PHONE = models.CharField(max_length=15)
    SEND_PHONE = models.CharField(max_length=15)
    MSG_BODY = models.TextField()

    class Meta:
        db_table = 'BIZ_MSG'