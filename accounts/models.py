from django.db import models
from django.contrib.auth.models import AbstractUser
from Todo_Api.basemodel import TimeBaseModel
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 
from datetime import datetime,timedelta
from .usermanager import CustomUserManager
import jwt
from django.conf import settings

class User(AbstractUser):
    username = None 
    email = models.EmailField(_("email address"), blank=False, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    email_verified = models.BooleanField(
        _("email_verfied"),
        default=True,
        help_text=_(
            "Designates whether this users email is verified. "
        ),
    )
    date_joined = models.DateTimeField(_("Date Joined"),auto_now_add=True) 
    last_joined = models.DateTimeField(_("Last Joined"), auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email if self.email else ""

    
    @property 
    def token(self):
        token=jwt.encode(
            {'email':self.email,'exp':datetime.utcnow() + timedelta(hours=24)},settings.SECRET_KEY,
            algorithm='HS256')

        return token


