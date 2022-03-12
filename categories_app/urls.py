from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet

router = DefaultRouter()
router.register(r"categories", CategoriesViewSet, basename="Categories")
urlpatterns = router.urls