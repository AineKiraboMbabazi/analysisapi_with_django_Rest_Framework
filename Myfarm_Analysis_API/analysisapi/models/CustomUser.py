from django.contrib.auth.models import AbstractUser
from analysisapi.models.association import Association
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    associationId = models.ForeignKey(Association,on_delete = models.CASCADE)
    # governmentId = models.ForeignKey(Association,on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    user_group = models.CharField(max_length=20)
    user_role = models.CharField(max_length=20)
    created_by = name
    creation_date = models.DateTimeField(auto_now=True)

    user = {
        "associationId":associationId,
        "name":name,
        "status":status,
        "email":email,
        "country":country,
        "password":password,
        "user_group":user_group,
        "user_role":user_role,
        "created_by":created_by,
        "creation_date":creation_date
    }

    def __str__(self):
        return self.user
    

    objects = models.Manager()