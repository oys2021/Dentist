# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.db import models
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager


# class Administrator(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

# # # Create your custom user models here.
# # class Administrator(AbstractBaseUser, PermissionsMixin):
# #     fullname=models.CharField(max_length=250)
# #     title=models.CharField(max_length=250)
# #     email_address=models.CharField(unique=True)

# #     username = None
# #     USERNAME_FIELD = "email_address"
# #     picture=models.ImageField()
# #     created_at=models.DateTimeField(auto_now_add=True)
# #     updated_at=models.DateTimeField(auto_now=True)
# #     objects = AdministratorManager()
# #     is_staff = models.BooleanField(default=False)
# #     is_superuser = models.BooleanField(default=False)
# #     is_active = models.BooleanField(default=True)

#     # class Meta:
#     #     db_table = "users"

#     # def __str__(self):
#     #     return self.fullname or self.email_address

# # https://testdriven.io/blog/django-custom-user-model/
