from django.db import models
class AdminUsername(models.Model):
    username=models.CharField(max_length=200)
    def __str__(self):
        return self.username

class AdminPassword(models.Model):
    models.ForeignKey(AdminUsername,on_delete=models.CASCADE)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.password

class Users(models.Model):
    name=models.CharField(max_length=200)
    phonenumber=models.TextField(max_length=13)
    email=models.EmailField()
