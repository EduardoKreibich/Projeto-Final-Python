from django.db import models
import uuid


class Student_Couse_Status(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    status = models.CharField(
        max_length=10,
        choices=Student_Couse_Status.choices,
        default=Student_Couse_Status.PENDING,
    )
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="students_courses"
    )
    student = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="students_courses"
    )
