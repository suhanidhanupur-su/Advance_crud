from django.db import models

# Create your models here.
# class Student(models.Model):
#     std_name = models.CharField(max_length=100)
#     std_roll = models.IntegerField()
#     std_image = models.ImageField(upload_to='students/')
#     std_city = models.CharField(max_length=100)

#     def __str__(self):
#         return self.std_name

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    roll_no = models.CharField(max_length=20)
    image = models.ImageField(upload_to='students/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)