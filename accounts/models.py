from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False)
    my_courses = models.ManyToManyField(
        "courses.Course",
        related_name="students",
        through="students_courses.StudentCourse",
    )
