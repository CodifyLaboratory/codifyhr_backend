from .views import ResumeReadOnlyModelViewSet, WishlistModelViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r"resumes", ResumeReadOnlyModelViewSet, basename='resumes')
urlpatterns = router.urls


urlpatterns += [
    path('wishlist/', WishlistModelViewSet.as_view({'get': 'list'})),
    path('wishlist/<int:pk>/', WishlistModelViewSet.as_view({'get': 'retrieve'})),
    path('wishlist/create/<int:pk>/', WishlistModelViewSet.as_view({'post': 'create'})),
    path('wishlist/delete/<int:pk>/', WishlistModelViewSet.as_view({'delete': 'destroy'}))
]