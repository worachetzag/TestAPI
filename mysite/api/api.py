from django.db import router
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Activities, Profile
from .serializers import ActivitiesSerializers, Profileserializers

class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializers

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = Profileserializers
    

router = routers.DefaultRouter()
router.register(r'activities/list', ActivitiesViewSet)
router.register(r'profile/list', ProfileViewSet)