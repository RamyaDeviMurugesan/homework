from datetime import timezone
from enum import Enum
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User

#enums.py
class Grade(Enum):

    X = "X"
    # ELEVENTH = "XI"
    # TWELTH = "XII"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    
class Section(Enum):

    A = "A"
    B = "B"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class Role(Enum):

    STUDENT = "Student"
    TEACHER = "Teacher"
    # ELEVENTH = "XI"
    # TWELTH = "XII"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=255, choices=Grade.choices())
    section = models.CharField(max_length=10, choices=Section.choices())
    role = models.CharField(max_length=100, choices=Role.choices())

    def __str__(self):
        return self.user.username

def validate_homeworkdate(value):
    """Ensure homework date is today or in the future."""
    if value < timezone.now().date():
        raise ValidationError("Homework date cannot be in the past.")

class HomeWork(models.Model):
    grade = models.CharField(max_length=255, choices=Grade.choices())
    section = models.CharField(max_length=10, choices=Section.choices())
    hwDate = models.DateField(validators=[validate_homeworkdate])
    subject  = models.CharField(max_length=255, default="")
    tasks  = models.CharField(max_length=500,  default="")
    added_by  = models.CharField(max_length=255,  default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.hwDate
    
class SchoolDetails(models.Model):
    grade = models.CharField(max_length=255, choices=Grade.choices())
    section = models.CharField(max_length=10, choices=Section.choices())
    subject = models.BigIntegerField()
    noOfStudents = models.IntegerField(default=0)

    def __str__(self):
        return "Classroom Details"
    
class HomeWorkArchive(models.Model):
    grade = models.CharField(max_length=255, choices=Grade.choices())
    section = models.CharField(max_length=10, choices=Section.choices())
    hwDate = models.DateField(validators=[validate_homeworkdate])
    homework  = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
