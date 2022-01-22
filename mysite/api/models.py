from ast import walk
from django.db import models
from django.contrib.auth.models import User


class Activities(models.Model):
    health = models.CharField(max_length=200)
    heart_rate = models.IntegerField()
    walk_count = models.IntegerField()

    def __str__(self):
        return str(self.health) + ' , ' + str(self.heart_rate)+ ' , ' + str(self.walk_count)


class Profile(models.Model):
    profile = models.OneToOneField(User,
                                  on_delete=models.CASCADE,
                                  related_name='profile_profile')
    activities = models.ForeignKey(Activities,
                                  on_delete=models.CASCADE,
                                  related_name='profile_activities')
    friends = models.ManyToManyField(User,
                                  related_name='profile_friends',
                                  blank=True)                             
    

