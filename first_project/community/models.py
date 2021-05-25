from django.db import models

# Create your models here.

class Human(models.Model):
    last_name = models.CharField(max_length=264,unique=True)
    first_name = models.CharField(max_length=264)
    email = models.EmailField()

    def __str__(self):
        return self.last_name + ", " + self.first_name

    class Meta:
        app_label = "community"
