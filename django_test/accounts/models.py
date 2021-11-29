from django.db import models

# Create your models here.


class User(models):
    username = models.CharField('用户名', max_length=64)
    password = models.CharField('密码', max_length=256)

    class Meta:
        db_table = "accounts_user"
