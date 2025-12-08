from dataclasses import fields
from rest_framework import serializers
from .models import User

from .models import Room,RoomImage,OccupiedDate

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


class OccupiedDateSeralizer(serializers.HyperlinkedModelSerializer):
    room = serializers.HyperlinkedRelatedField(view_name ='room-detail',queryset = Room.objects.all())
    class Meta:
        model = OccupiedDate
        fields = ['url','id','room','date']


from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username','password','email','full_name']

         
    def validate_password(self, value):
        return make_password(value)