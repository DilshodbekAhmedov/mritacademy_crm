from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django_resized import ResizedImageField
from .validators import phone_validator

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Berilgan elektron pochta va parol bilan foydalanuvchi yaratadi va saqlaydi.
        """
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return  user

    def _create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_active
        user.save()
        return user
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault(("is_active", True))

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuserda bo'lishi kerak is_staff = True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuserda bo'lishi kerak is_superuser = True.")
        return self._create_user(username, password, **extra_fields)

class User(AbstractBaseUser):
    USER_TYPE = (
        ("superuser", "Superuser"),
        ("admin", "Admin"),
        ("teacher", "O'qutuvchi"),
        ("user", "Foydalanuvchi"),
    )
    first_name = models.CharField(max_length=255, blank=True, verbose_name="Ism")
    last_name = models.CharField(max_length=255, blank=True, verbose_name="Familiya")
    avatar = ResizedImageField(verbose_name="Rasim",
                               size=[500, 400],
                               crop=["middle", "center"],
                               null=True, blank=True,
                               upload_to="user_avatars/")
    email = models.EmailField(unique=True, blank=True, verbose_name="Pochta")
    username = models.CharField(max_length=255, unique=True, verbose_name="username")
    is_staff =models.BooleanField(default=False, verbose_name="Xodimlarning holati")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    birthday =models.DateField(null=True, blank=True, verbose_name="Tug'ilgan kun")
    phone = models.CharField(max_length=13, null=True, blank=True, validators=[phone_validator,], verbose_name="Telefon raqam")
    user_type = models.CharField(max_length=50, choices=USER_TYPE, default="user", verbose_name="Foydalanuvchi turi")

    USERNAME_FIELD = "username"
    objects = MyUserManager

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name}-{self.last_name}"

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"







