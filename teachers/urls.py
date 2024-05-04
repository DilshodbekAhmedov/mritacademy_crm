from django.urls import path
from .views import TeacherViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'teachers', TeacherViewSet)

urlpatterns = []


