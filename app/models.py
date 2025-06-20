from django.db import models


class UserRole(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
