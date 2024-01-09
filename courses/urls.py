from django.urls import path
from . import views
from contents import views as content_views
from students_courses import views as students_views

urlpatterns = [
    path("courses/", views.CourseView.as_view()),
    path("courses/<str:pk>/", views.CourseDetailView.as_view()),
    path("courses/<str:pk>/contents/", content_views.ContentView.as_view()),
    path(
        "courses/<str:pk>/contents/<str:content_id>/",
        content_views.ContentDetailView.as_view(),
    ),
    path("courses/<str:pk>/students/", students_views.StudentDetailView.as_view()),
]
