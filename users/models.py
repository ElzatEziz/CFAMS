from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', '系统管理员'),
        ('manager', '资产管理人员'),
        # 可以根据需要添加更多角色
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='用户')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='manager', verbose_name='角色')
    phone = models.CharField(max_length=20, blank=True, verbose_name='电话号码')
    department = models.CharField(max_length=100, blank=True, verbose_name='部门')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '用户资料'
        verbose_name_plural = '用户资料'


# Django信号，用于在创建新的User实例时自动创建UserProfile实例
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
