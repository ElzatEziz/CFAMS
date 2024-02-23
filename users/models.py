from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)
    
class User(AbstractBaseUser):
    ROLE_CHOICES = (
        ('admin', '系统管理员'),
        ('manager', '资产管理人员'),
        # 可以根据需要添加更多角色
    )
    username=models.CharField(max_length=20,verbose_name='用户名',unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='manager', verbose_name='角色')
    phone = models.CharField(max_length=20, blank=True, verbose_name='电话号码')
    department = models.CharField(max_length=100, blank=True, verbose_name='部门')
    email = models.EmailField(blank=True,verbose_name="电子邮件")
    USERNAME_FIELD="username"
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table="tb_users"
        verbose_name = '用户'
        verbose_name_plural = verbose_name

