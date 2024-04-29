from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Work(models.Model):
    link = models.URLField()
    work_type = models.CharField(max_length=10, choices = [('YT', 'Youtube'), ('IG', 'Instagram'), ('Other', 'Other')])

    def __str__(self):
        return self.work_type
    
class Artist_t(models.Model):
    name = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work = models.ManyToManyField(Work)

    def __str__(self):
        return self.name