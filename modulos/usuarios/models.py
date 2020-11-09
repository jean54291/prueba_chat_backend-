from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
# from .managers import UserManager

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, unique=True, verbose_name="Nombre de usuario")
    first_name = models.CharField(max_length=100, default='', verbose_name="Nombre")
    last_name = models.CharField(max_length=100, default='', verbose_name="Apellidos")
    email = models.EmailField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sk = models.CharField(max_length=100, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)
    en_linea = models.BooleanField(default=False)
    fecha_ultima_sesion = models.DateTimeField(null=True, blank=True, auto_now=True)
    objects = UserManager()
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    
    
    

    
    def nombreCompleto(self):
        txt = "{0} {1}"
        return txt.format(self.first_name, self.last_name)
    
    def __str__(self):
        return self.nombreCompleto()

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        db_table = 'auth_user'