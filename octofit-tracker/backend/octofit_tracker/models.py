from djongo import models
from djongo.models import ObjectIdField

class User(models.Model):
    _id = ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Team(models.Model):
    _id = ObjectIdField()
    name = models.CharField(max_length=255)
    members = models.JSONField()

class Activity(models.Model):
    _id = ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    _id = ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    _id = ObjectIdField()
    name = models.CharField(max_length=255)
    description = models.TextField()
