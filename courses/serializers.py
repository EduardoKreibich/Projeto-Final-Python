from rest_framework import serializers
from .models import Course
from students_courses.serializers import StudentCourseSerializer
from accounts.models import Account
from accounts.serializers import AccountSerializer
from contents.serializers import ContentSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "contents": {"read_only": True},
            "students_courses": {"read_only": True},
        }


class CourseStudentsSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "students_courses",
        ]
        extra_kwargs = {
            "name": {"read_only": True},
        }

    def update(self, instance, validated_data):
        students = []
        student_not_found = []
        for student_course in validated_data["students_courses"]:
            student = student_course["student"]
            student_found = Account.objects.filter(email=student["email"]).first()
            if not student_found:
                student_not_found.append(student["email"])
            else:
                students.append(student_found)
        if student_not_found:
            raise serializers.ValidationError(
                {
                    "detail": f"No active accounts was found: {', '.join(student_not_found)}."
                }
            )
        instance.students.add(*students)
        return instance


class CourseDetailSerializer(serializers.ModelSerializer):
    instructor = AccountSerializer(read_only=True)
    students_courses = StudentCourseSerializer(read_only=True, many=True)
    contents = ContentSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
