from django.db import models
import datetime

# Create your models here.

class Userinfo(models.Model):
    username = models.CharField(max_length=20)
    fullname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.IntegerField()
    join_time = models.DateTimeField(auto_now_add=True)
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    depart = models.ForeignKey(to='Department',to_field='id',on_delete=models.CASCADE)

class Department(models.Model):
    '''部门表'''
    id = models.BigAutoField(verbose_name='ID', primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=20)