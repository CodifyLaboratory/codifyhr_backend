from .views import ResumeViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"resumes", ResumeViewSet, basename='resumes')
urlpatterns = router.urls
