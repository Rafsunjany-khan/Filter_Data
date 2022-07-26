from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    reg_name = models.IntegerField(max_length=10)
    student_roll_no = models.IntegerField(max_length=10)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=11)

    def __str__(self):
        return self.student_name







