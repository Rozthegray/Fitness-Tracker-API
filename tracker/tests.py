from django.test import TestCase
from django.contrib.auth.models import User
from .models import Activity

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        activity = Activity.objects.create(
            user=user,
            activity_type='Running',
            duration=30,
            distance=5,
            calories_burned=300,
            date='2025-04-06'
        )
        self.assertEqual(activity.activity_type, 'Running')
