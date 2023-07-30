from django.db import models
import random

Status = ((0, "Draft"),(1,"Published"))
# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    journal_file = models.FileField(upload_to='globabrain_journal/')
    status = models.IntegerField(choices=Status, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    class Meta:
        ordering =['-created_on']
