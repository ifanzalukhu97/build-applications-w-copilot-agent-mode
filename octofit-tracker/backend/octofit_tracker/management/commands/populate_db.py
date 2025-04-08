from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta, date
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(**settings.DATABASES['default']['CLIENT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@mhigh.edu', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team')
        team2 = Team(_id=ObjectId(), name='Gold Team')
        team1.save()
        team2.save()
        team1.members.add(users[0], users[1])
        team2.members.add(users[2], users[3], users[4])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], type='Cycling', duration=timedelta(hours=1), date=date.today()),
            Activity(_id=ObjectId(), user=users[1], type='Crossfit', duration=timedelta(hours=2), date=date.today()),
            Activity(_id=ObjectId(), user=users[2], type='Running', duration=timedelta(hours=1, minutes=30), date=date.today()),
            Activity(_id=ObjectId(), user=users[3], type='Strength', duration=timedelta(minutes=30), date=date.today()),
            Activity(_id=ObjectId(), user=users[4], type='Swimming', duration=timedelta(hours=1, minutes=15), date=date.today()),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=95),
            Leaderboard(_id=ObjectId(), user=users[3], score=85),
            Leaderboard(_id=ObjectId(), user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), user=users[0], description='Cycling Training', date=date.today()),
            Workout(_id=ObjectId(), user=users[1], description='Crossfit Training', date=date.today()),
            Workout(_id=ObjectId(), user=users[2], description='Running Training', date=date.today()),
            Workout(_id=ObjectId(), user=users[3], description='Strength Training', date=date.today()),
            Workout(_id=ObjectId(), user=users[4], description='Swimming Training', date=date.today()),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
