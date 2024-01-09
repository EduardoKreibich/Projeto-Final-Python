from rest_framework.generics import RetrieveUpdateAPIView
from courses.models import Course
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin

from courses.serializers import CourseStudentsSerializer


class StudentDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = CourseStudentsSerializer
    queryset = Course.objects.all()
