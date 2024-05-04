from rest_framework import routers
from .views import CourseViewSet


router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet)
urlpatterns = router.urls