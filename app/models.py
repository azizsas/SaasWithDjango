from django.db import models
"""
# Create your models here.
class Visit(models.Model):
     #db table
     #id primary key auto increment ,its hidden 
    path=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
"""
class PageVisit(models.Model):
     #db table
     #id primary key auto increment ,its hidden 
    path=models.TextField(blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)

