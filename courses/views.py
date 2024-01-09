from .serializers import CourseSerializer, CourseDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Course
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAccountAdminOrAuth


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountAdminOrAuth]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Course.objects.filter(students=self.request.user)
        return self.queryset.all()


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountAdminOrAuth]
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
