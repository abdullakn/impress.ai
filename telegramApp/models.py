from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MsgCount(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    stupid=models.IntegerField(default=0)
    fat=models.IntegerField(default=0)
    dump=models.IntegerField(default=0)


