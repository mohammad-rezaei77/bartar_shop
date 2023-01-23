from django.db import models
from datetime import datetime
# Create your models here.

class Discount(models.Model):
    name = models.CharField(max_length=10)
    code= models.CharField(max_length=100)
    desc = models.TextField()
    amount = models.FloatField()
    type = models.CharField(
        max_length=10,
        choices=(
            ('percent','percent'),
            ('fix','fix')),default='percent')
    start = models.DateTimeField(blank=True, null=True)
    expire = models.DateTimeField(blank=True, null=True)
    number = models.IntegerField(default=0)
    remaining = models.IntegerField(default=0)
    
    is_unexpired = models.BooleanField(default=False)
    is_unlimited = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titile
    def verify(self):
        
        if self.is_active:
            return True
        
        if self.is_unexpired and self.is_unlimited:
            return True
        
        if not self.is_unexpired:
            now = datetime.now()
            if self.start < now and self.expire > now:
                return True
            return False

        if not self.is_unlimited:
            if self.number > 0:
                if self.remaining > 0:
                    self.remaining -= 1
                    self.save()
                    return True

            return False
    