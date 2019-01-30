from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 100)
    age = models.CharField(max_length = 10)
    experience = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
