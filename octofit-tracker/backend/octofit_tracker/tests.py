from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email='test@example.com', password='password123')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Team A')
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(type='Running', duration='00:30:00', date='2025-04-08')
        self.assertEqual(activity.type, 'Running')

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(description='Push-ups', date='2025-04-08')
        self.assertEqual(workout.description, 'Push-ups')