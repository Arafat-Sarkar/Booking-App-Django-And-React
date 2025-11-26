from dataclasses import fields
from rest_framework import serializers

from .models import Room,RoomImage

class RoomImageSeralizer(serializers.ModelSerializer):
    room = serializers.HyperlinkedRelatedField(view_name = 'room-detail',queryset= Room.objects.all()),
    
    class Meta:
        model = RoomImage
        fields = ['id','image','caption', 'room']


class RoomSeralizer(serializers.HyperlinkedModelSerializer):
    images = RoomImageSeralizer(many=True , read_only = True)
    class Meta:
        model = Room
        fields = ['url', 'id', 'name','type','PricePerNight', 'currency','maxOccupancy', 'description','images']