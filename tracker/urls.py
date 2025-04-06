from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, UserViewSet, RegisterView

router = DefaultRouter()
router.register('activities', ActivityViewSet, basename='activity')
router.register('users', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]
