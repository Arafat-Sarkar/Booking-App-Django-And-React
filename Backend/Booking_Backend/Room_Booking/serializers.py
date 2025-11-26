from dataclasses import fields
from rest_framework import serializers

from .models import Room

class RoomSeralizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['url', 'id', 'name','type','PricePerNight', 'currency','maxOccupancy', 'description']