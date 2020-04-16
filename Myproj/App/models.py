from django.db import models

# Create your models here.
class Users(models.Model):
    Name=models.CharField(max_length=344,unique=True)
    Fav_Movie=models.CharField(max_length=344,unique=True)
    Fav_Book=models.CharField(max_length=344,unique=True)
    Fav_Food=models.CharField(max_length=344,unique=True)

    def __str__(self):
        return self.Name
