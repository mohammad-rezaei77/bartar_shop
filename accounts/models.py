from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
"""
 UserManager
"""
class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authenticated instead of username
    """
    
    def create_user(self, email, password, **extra_fields):
        """create and save User with the given email and password and extra data"""
        if not email :
            raise ValueError(_("the email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """create and save SuperUser with the given email and password"""
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)  
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError (_("superuser must have is_staff= True."))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError (_("SuperUser must have is_superuser= True.")) 
        return self.create_user(email, password, **extra_fields)


class User (AbstractBaseUser,PermissionsMixin):
    """
    Custom User Model for our app
    """
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # is_verified = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    def __str__ (self):
        return self.email
    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    def __str__ (self):
        return self.user.email
    
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created :
        Profile.objects.create(user=instance)