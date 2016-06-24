from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# class Manager(UserManager):
#     def create_user(self, nickname, email, password):
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#             nickname=nickname,
#             password=password,
#         )
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, nickname, email, password):
        
#         user = self.model(
#             email=self.normalize_email(email),
#             nickname=nickname,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

class User(AbstractUser):
    nickname = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
#    objects = Manager()
