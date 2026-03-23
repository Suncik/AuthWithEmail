from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from datetime import timedelta


# 🔹 MANAGER (tepada bo‘lishi shart)
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Email required')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.is_active = False
        user.save()
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_verified = True
        user.save()
        return user


# 🔹 USER MODEL
class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()   

    def __str__(self):
        return self.email


# 🔹 EMAIL VERIFICATION MODEL
class EmailVerification(models.Model):
    TYPE_CHOICES=(
        ('verify', 'verify'),
        ('reset', 'Reset Password'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    type=models.CharField(max_length=10, choices=TYPE_CHOICES, default='verify')
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self): 
        return timezone.now() > self.created_at + timedelta(minutes=5)

    def __str__(self):
        return f"{self.user.email} - {self.code}"