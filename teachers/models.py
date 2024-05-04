from django.db import models
# from courses.models import Course

from django.contrib.auth.models import User

# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone1 = models.CharField(max_length=100)
    phone2 = models.CharField(max_length=100)
    family_phone = models.CharField(max_length=100)
    resume = models.FileField(upload_to='teachers/')
    # course = models.ManyToManyField(Course, related_name='teachers', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


