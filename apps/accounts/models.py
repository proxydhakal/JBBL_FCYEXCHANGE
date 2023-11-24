from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password



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
    client_code = models.CharField(max_length=10, blank=True, null=True, default='-')
    branch = models.CharField(max_length=10, blank=True, null=True, default='-')
    profile_image = models.ImageField(default='profile_pics/default.png', upload_to='media/profile_pics')
    is_staff = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=USER_STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    company = models.CharField(max_length=254,null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True, default='-')
    dob = models.DateField(blank=True, null=True, default='2022-02-02')
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        # Check if the profile_image is set and email exists
        if self.email and not self.profile_image:
            # Extract the text before '@' symbol from the email
            email_parts = self.email.split('@')
            if len(email_parts) == 2:
                email_prefix = email_parts[0]
            else:
                email_prefix = "default"  # Default name if email format is not as expected

            # Construct the new profile image filename
            filename = f"profile_pics/{email_prefix}.png"

            # Set the profile_image field to the new filename
            self.profile_image.name = filename
        elif not self.profile_image:
            # Set the profile_image to default.png if not provided by the user
            self.profile_image.name = 'profile_pics/default.png'

        super(UserAccount, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = "USER ACCOUNT"
        verbose_name_plural = "USER ACCOUNTS"

