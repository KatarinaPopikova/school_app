from django.urls import path
from . import views
from django.urls.conf import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('teachers', views.TeacherViewSet)
router.register('subjects', views.SubjectViewSet)
router.register('students', views.StudentViewSet)

urlpatterns = [
     path('', include(router.urls))
]
