from django.db import models
import django_filters
# Create your models here.

class Course(models.Model):
    MAIN_STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=MAIN_STATUS, default='active')

    def __str__(self):  
        return self.name
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
