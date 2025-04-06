from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, UserViewSet

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
