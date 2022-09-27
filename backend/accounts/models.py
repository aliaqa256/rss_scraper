from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
import re
from django.core.exceptions import ValidationError


def username_validator(value):
    reg = re.compile('^[\w._]+$')
    if not reg.match(value) or len(value)<4:
        raise ValidationError(u'%s please enter a valid username' % value)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        if not username:
            raise ValueError("Users must have username")
        if not password:
            raise ValueError("Users must have password")
        if not email:
            raise ValueError("Users must have email")
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, username, email, password, **kwargs):
        user = self.model(username=username, email=email, staff=True, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **kwargs):
        user = self.model(username=username, email=email,
                          staff=True, superuser=True, active=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


# Model User --------------------------------------------------------------------
class User(AbstractBaseUser):
    full_name = models.CharField(
        verbose_name='full name', max_length=250, blank=False, null=False)
    username = models.CharField(verbose_name='username', max_length=200,validators =[username_validator], db_index=True, null=False, blank=False,unique=True)
    email = models.EmailField(verbose_name='email',blank=False, null=False, unique=True)
    superuser = models.BooleanField(verbose_name='is superuser', default=False)
    staff = models.BooleanField(verbose_name='is staff', default=False)
    active = models.BooleanField(verbose_name='active', default=True)
    created_date = models.DateTimeField(
        verbose_name='created date', auto_now_add=True)
    update_date = models.DateTimeField(
        verbose_name='update date', auto_now=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.superuser

    @property
    def is_staff(self):
        return self.staff


    def __str__(self):
        return "{}".format(self.username)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        ordering = ('id', 'created_date',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'