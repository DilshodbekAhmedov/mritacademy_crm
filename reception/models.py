from django.db import models


class Reception(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    courses = models.ForeignKey(Course, on_delete=models.PROTECT)
    time = models.CharField(max_length=10)
    w_time = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.course}'
