
from django.db import models

class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=25)
    student_first_name = models.CharField(max_length=256)
    student_last_name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'student'