from django.db import models

# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str___(self):
        return self.title
