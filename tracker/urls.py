from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView, UserActivityListView, UserActivityDetailView, ActivitySummaryView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activities/', UserActivityListView.as_view(), name='activity-list'),
    path('activities/<int:pk>/', UserActivityDetailView.as_view(), name='activity-detail'),
    path('activities/summary/', ActivitySummaryView.as_view(), name='activity-summary'),
]
