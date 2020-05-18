from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    name      = models.CharField(max_length=100)
    location  = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('school:school_list')   

class Student(models.Model):
    name      = models.CharField(max_length=100)
    school    = models.ForeignKey(School,on_delete=models.CASCADE,related_name='student_school')

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('school:school_list')