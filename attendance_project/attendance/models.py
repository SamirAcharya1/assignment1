from django.db import models

# Create your models here.

class Classroom(models.Model):
    class_name = models.CharField(max_length=30)
    credit = models.IntegerField()

    def __str__(self):
        return f"{self.class_name} has {self.credit} credit"

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    roll_number = models.CharField(max_length=10, unique=True)
    class_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} is in {self.class_id.class_name}"

class Attendance(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_id.first_name} is {'Present' if self.present else 'Absent'} on {self.date}"
