from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)
    course = models.CharField(max_length=70)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return self.name