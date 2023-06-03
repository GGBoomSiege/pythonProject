from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="余额", max_digits=10, decimal_places=2, default=0)
    depart = models.ForeignKey("Department", verbose_name="部门",to_field='id', on_delete=models.CASCADE)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    create_time = models.DateTimeField(verbose_name="入职时间")

class Department(models.Model):
    title = models.CharField(verbose_name="部门名称", max_length=16, unique=True, null=False, blank=False, db_index=False)
    def __str__(self):
        return self.title
