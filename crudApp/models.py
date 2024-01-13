from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

