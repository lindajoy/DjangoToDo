from django.db import models

# Create your models here.
class list(models.Model):
    Title =  models.CharField(max_length=300)
    Description = models.CharField(max_length=600)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now = True)

    def  __str__(self):
        return "{}".format(self.Title)