from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_data
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        users = {}
        for user_data in test_data['users']:
            user = User.objects.create(
                _id=ObjectId(),
                email=user_data['email'],
                name=user_data['username']
            )
            users[user_data['username']] = user

        # Populate teams
        for team_data in test_data['teams']:
            team = Team.objects.create(
                _id=ObjectId(),
                name=team_data['name'],
                members=[{"username": users[member_username].name, "email": users[member_username].email} for member_username in team_data['members']]
            )

        # Populate activities
        for activity_data in test_data['activities']:
            duration_parts = activity_data['duration'].split(':')
            duration_in_minutes = int(duration_parts[0]) * 60 + int(duration_parts[1])
            Activity.objects.create(
                _id=ObjectId(),
                user=users[activity_data['user']],
                activity_type=activity_data['activity_type'],
                duration=duration_in_minutes
            )

        # Populate leaderboard
        for leaderboard_data in test_data['leaderboard']:
            Leaderboard.objects.create(
                _id=ObjectId(),
                user=users[leaderboard_data['user']],
                score=leaderboard_data['score']
            )

        # Populate workouts
        for workout_data in test_data['workouts']:
            Workout.objects.create(
                _id=ObjectId(),
                name=workout_data['name'],
                description=workout_data['description']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
