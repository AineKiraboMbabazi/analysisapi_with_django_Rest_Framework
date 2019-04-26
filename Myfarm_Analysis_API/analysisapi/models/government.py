from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Government(models.Model):
    """Government class defining the association model"""
      
    userId = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    Location = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    # created_by =userId
    creation_date =  models.DateTimeField(auto_now=True)
    
    government = {
        "userId":userId,
        "name":name,
        "location":Location,
        "status":status,
        # "created_by":created_by,
        "creation_date":creation_date
    }

    
    # def __str__(self):
    #     return self.government

    objects = models.Manager()