from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=22) # 默认值为22
    data = models.IntegerField(null=True, blank=True) # 默认为空

class Department(models.Model):
    title = models.CharField(max_length=16)

