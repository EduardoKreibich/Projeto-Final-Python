from django.db import models
import uuid


class Couse_Status(models.TextChoices):
    NOTSTARTED = "not started"
    INPROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11,
        choices=Couse_Status.choices,
        default=Couse_Status.NOTSTARTED,
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
    )
