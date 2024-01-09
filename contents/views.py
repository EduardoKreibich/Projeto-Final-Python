from .serializers import ContentSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Content
from courses.models import Course
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from courses.permissions import IsAccountAdminOrAuth
from .permissions import IsAccountAdminOrStudent
from rest_framework.exceptions import NotFound


class ContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountAdminOrAuth]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

    def perform_create(self, serializer):
        return serializer.save(course_id=self.kwargs.get("pk"))


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountAdminOrStudent]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

    def get_object(self):
        content = Content.objects.filter(pk=self.kwargs.get("content_id")).first()
        course = Course.objects.filter(pk=self.kwargs.get("pk"))
        if not content:
            raise NotFound({"detail": "content not found."})
        if not course:
            raise NotFound({"detail": "course not found."})
        self.check_object_permissions(self.request, content)
        return content
