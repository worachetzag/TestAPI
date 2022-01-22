from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Activities, Profile

class ActivitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ('id',
                  'health',
                  'heart_rate',
                  'walk_count')

# class FriendSerializers(serializers.ModelSerializer):

#     class Meta:
#         model = Activities
#         fields = ('activities')

class Profileserializers(serializers.ModelSerializer):
    activities = ActivitiesSerializers()
    # friends = FriendSerializers()
    
    class Meta:
        model = Profile
        fields = ('profile',
                  'activities',
                  'friends')