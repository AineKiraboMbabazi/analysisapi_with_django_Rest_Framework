from django.db import models
from django.contrib.auth.models import User
from analysisapi.models.government import Government

# Create your models here.
class Association(models.Model):
    """Association class defining the association model"""
    governmentId = models.ForeignKey(Government, related_name='choices', on_delete=models.CASCADE)
    userId = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    Location = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    # created_by =userId
    creation_date =  models.DateTimeField(auto_now=True)
    
    association = {
        "governmentId":governmentId,
        "userId":userId,
        "name":name,
        "location":Location,
        "status":status,
        # "created_by":created_by,
        "creation_date":creation_date
    }

    # def __str__(self):
    #     return self.association

    objects = models.Manager()

        