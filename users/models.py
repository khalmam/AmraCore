from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', _('Admin')),
        ('designer', _('Designer')),
        ('customer', _('Customer')),
    ]

    role = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES, 
        default='customer'
    )
    
    email = models.EmailField(_('email address'), unique=True)
    
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False, # Now allows non-unique, since email is the true unique field
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        blank=True,
        null=True,
    )
    
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # We keep this for createsuperuser ease, but now it can be left blank

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.email