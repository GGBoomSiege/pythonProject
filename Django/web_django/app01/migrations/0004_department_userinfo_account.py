# Generated by Django 4.2.1 on 2023-05-30 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_delete_department_rename_name_userinfo_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='account',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='账户余额'),
        ),
    ]
