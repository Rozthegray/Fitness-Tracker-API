from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User, Activity
from .serializers import UserSerializer, ActivitySerializer
from django.shortcuts import get_object_or_404

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserActivityListView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

class ActivitySummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        activities = Activity.objects.filter(user=request.user)
        total_duration = sum(activity.duration for activity in activities)
        total_distance = sum(activity.distance or 0 for activity in activities)
        total_calories = sum(activity.calories_burned for activity in activities)

        return Response({
            "total_duration": total_duration,
            "total_distance": total_distance,
            "total_calories": total_calories
        })
