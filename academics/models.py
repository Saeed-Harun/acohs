from django.db import models
from accounts.models import CustomUser

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    credit = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"

class Result(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    def grade(self):
        if self.score >= 80:
            return 'A'
        elif self.score >= 70:
            return 'B'
        elif self.score >= 60:
            return 'C'
        elif self.score >= 50:
            return 'D'
        else:
            return 'F'

    def gpa_point(self):
        return {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }[self.grade()]

    def __str__(self):
        return f"{self.student.username} - {self.course.code} - {self.score}"
