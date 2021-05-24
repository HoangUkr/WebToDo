from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=True)
    is_Verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS = (
        ('IN PROGRESS', 'IN PROGRESS'),
        ('SUCCEED', 'SUCCEED'),
        ('MISSED', 'MISSED'),
    )
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    task_name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=True)
    task_category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    due_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)


    def __str__(self):
        return self.task_name





