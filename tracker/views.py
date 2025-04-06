from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.contrib.auth.models import User
from .models import Activity
from .serializers import ActivitySerializer, UserSerializer
from .permissions import IsOwner

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date', 'duration', 'calories_burned']
    search_fields = ['activity_type']

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        queryset = self.get_queryset()
        summary = queryset.aggregate(
            total_duration=Sum('duration'),
            total_distance=Sum('distance'),
            total_calories=Sum('calories_burned'),
        )
        return Response(summary)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
