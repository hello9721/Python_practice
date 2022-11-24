from django.db import models
from django.utils import timezone

# Create your models here.
class Me(models.Model):

    title = models.CharField(max_length=20)
    date = models.DateTimeField()
    main = models.TextField()
    
    def publish(self):

        self.date = timezone.now()
        self.save()

    def __str__(self):

        return self.title

# {% static 'css/main.css' %}
# {% load static %}