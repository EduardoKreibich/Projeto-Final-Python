from rest_framework import serializers
from .models import StudentCourse


class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = ["id", "status", "student_id", "student_email", "student_username"]

    student_email = serializers.CharField(max_length=100, source="student.email")
    student_username = serializers.CharField(
        max_length=150,
        source="student.username",
        read_only=True,
    )
