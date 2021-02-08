from django.db import models


class Summary(models.Model):
    course_code = models.CharField(max_length=50)
    faculty=models.CharField(max_length=50)
    grade= models.CharField(max_length=10)
    gpa =models.FloatField(max_length=3)
    semester= models.CharField(max_length=20)

    def __str__(self) :
         return  self.course_code