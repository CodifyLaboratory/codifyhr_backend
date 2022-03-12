from rest_framework.routers import DefaultRouter
from .views import PartnerViewSet

router = DefaultRouter()
router.register(r"main", PartnerViewSet, basename='Partners')
urlpatterns = router.urls