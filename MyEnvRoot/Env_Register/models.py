from django.db import models


# Create your models here.


class EnvList_New(models.Model):

    VAPP=models.CharField(max_length=20)
    Release = models.CharField(max_length=10)
    BSS_Non_CPQ=models.CharField(max_length=20)
    CPQ_OSS_SIO=models.CharField(max_length=20)
    ARM=models.CharField(max_length=20)
    DB_SERVERS=models.CharField(max_length=500)
    COMMENTS=models.CharField(max_length=500)
    CREATION_DATE=models.DateTimeField(auto_now_add=True)



