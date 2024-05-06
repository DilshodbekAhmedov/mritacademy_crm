
from django.db import models
from courses.models import Course

class EnrollCourse(models.Model):
    DAYS = (
        ('mon_wed_fri', 'Monday, Wednesday, Friday'),
        ('tue_thu_sat', 'Tuesday, Thursday, Saturday'),
        ("everyday",'Everyday')
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    course = models.ForeignKey(Course, max_length=256, on_delete=models.PROTECT)
    time = models.CharField(max_length=10)
    days = models.CharField(max_length=40, choices=DAYS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.course}'
    