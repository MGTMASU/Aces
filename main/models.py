from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=150)
    userName = models.CharField(max_length=30)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name
