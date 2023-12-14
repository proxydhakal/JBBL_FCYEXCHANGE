from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from simple_history.models import HistoricalRecords
from import_export import resources
from simple_history import register
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
import inspect


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email')

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.role = UserAccount.SUPER_ADMIN
        user.set_password(password)
        user.save()
        return user



class UserAccount(AbstractBaseUser, PermissionsMixin):
    SUPER_ADMIN = 0
    USER = 1
    BRANCH_STAFF = 2

    INACTIVE = 'INACTIVE'
    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'

    USER_STATUS = (
        (INACTIVE, 'Inactive'),
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted')
    )

    ROLE_TYPES = (
        (SUPER_ADMIN, 'SUPER_ADMIN'),
        (USER, 'USER'),
        (BRANCH_STAFF, 'BRANCH_STAFF'),
    )

    role = models.IntegerField(choices=ROLE_TYPES, default=1)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    client_code = models.CharField(max_length=20, blank=True, null=True, default='-')
    branch = models.CharField(max_length=10, blank=True, null=True, default='-')
    profile_image = models.ImageField(default='profile_pics/default.png', upload_to='media/profile_pics')
    is_staff = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=USER_STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    company = models.CharField(max_length=254,null=False, blank=False, default='-')
    phone = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True, default='-')
    dob = models.DateField(blank=True, null=True, default='2022-02-02')
    history = HistoricalRecords()
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if self.email and not self.profile_image:
            email_parts = self.email.split('@')
            if len(email_parts) == 2:
                email_prefix = email_parts[0]
            else:
                email_prefix = "default" 

            filename = f"profile_pics/{email_prefix}.png"

            self.profile_image.name = filename
        elif not self.profile_image:
            self.profile_image.name = 'profile_pics/default.png'

        super(UserAccount, self).save(*args, **kwargs)
        
        
    class Meta:
        verbose_name = "USER ACCOUNT"
        verbose_name_plural = "USER ACCOUNTS"
        
        
class UserDetails(models.Model):
    BranchCode = models.CharField(max_length=5,blank=False, null=False)
    BranchName = models.CharField(max_length=255, blank=True, null=True)
    MainCode = models.CharField(max_length=20, blank=False, null=False)
    Name = models.CharField(max_length=255, blank=False, null=False)
    Address = models.CharField(max_length=255, blank=True, null=True, default='-')
    Pan = models.CharField(max_length=20, blank=True, null=True)
    Mobile = models.CharField(max_length=20, blank=True, null=True)
    history = HistoricalRecords()
    objects = UserAccountManager()
    
    def __str__(self):
        return f"{self.BranchCode}-{self.BranchName}-{self.MainCode}"
    
    class Meta:
        verbose_name = "USER DETAILS"
        verbose_name_plural = "USER DETAILS"


class UserDetailsResource(resources.ModelResource):
    class Meta:
        model = UserDetails
