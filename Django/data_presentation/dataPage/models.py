from django.db import models
import uuid
import datetime

def unique_user_id():
    unique_user_id_lst = [datetime.datetime.now().strftime('%Y%m%d'), str(uuid.uuid4().int % (10 ** 8))]
    unique_user_id = int(''.join(unique_user_id_lst))
    return unique_user_id

def unique_department_id():
    unique_department_id = uuid.uuid4().int % (10 ** 8)
    return unique_department_id

def unique_job_id():
    unique_job_id_lst = [datetime.datetime.now().strftime('%Y%m%d'), str(uuid.uuid4().int % (10 ** 8))]
    unique_job_id = int(''.join(unique_job_id_lst))
    return unique_job_id


# Create your models here.

class UserInfo(models.Model):
    id = models.BigIntegerField(primary_key=True,default=unique_user_id)
    username = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="余额", max_digits=10, decimal_places=2, default=0)
    depart = models.ForeignKey(to="Department", verbose_name="部门",to_field='id', null=True, blank=True, on_delete=models.SET_NULL)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    create_time = models.DateField(verbose_name="入职时间")

class Department(models.Model):
    id = models.BigIntegerField(primary_key=True,default=unique_department_id)
    title = models.CharField(verbose_name="部门名称", max_length=16, unique=True, null=False, blank=False, db_index=False)
    def __str__(self):
        return self.title

class BossJobs(models.Model):
    id = models.BigIntegerField(primary_key=True,default=unique_job_id)
    job_title = models.CharField(verbose_name="职位名称", max_length=50, null=False, blank=False)
    location = models.CharField(verbose_name="岗位地点", max_length=50, null=False, blank=False)
    salary = models.CharField(verbose_name="薪资待遇", max_length=50, null=False, blank=False)
    experience = models.CharField(verbose_name="工作经验要求", max_length=50, null=False, blank=False)
    education = models.CharField(verbose_name="教育背景要求", max_length=50, null=False, blank=False)
    hr = models.CharField(verbose_name="招聘人", max_length=50, null=False, blank=False)
    status = models.CharField(verbose_name="招聘人状态", max_length=50, null=True, blank=True)
    job_url = models.TextField(verbose_name="职位链接", null=True, blank=True)
    organization_name = models.CharField(verbose_name="公司名称", max_length=50, null=True, blank=True)
    organization_size = models.CharField(verbose_name="公司规模", max_length=50, null=True, blank=True)
    company_url = models.TextField(verbose_name="公司链接", null=True, blank=True)
    create_time = models.DateField(verbose_name="创建时间", default=datetime.datetime.now().strftime('%Y%m%d'))
