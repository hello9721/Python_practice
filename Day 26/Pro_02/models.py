from django.db import models
from django.utils import timezone

# Create your models here.

class Info(models.Model):

    code = models.IntegerField()
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    models = models.CharField(max_length=250)
    
    # makemigration -> migrate 하고 나면 db에 테이블이 생성됨.
    # Pro_02_info

    def __str__(self):
        return self.name

class Blog(models.Model):

    title = models.CharField(max_length=20)
    date = models.DateTimeField()
    main = models.TextField()
    
    def publish(self):

        self.date = timezone.now()
        self.save()

    def __str__(self):

        return self.title
