from django.contrib.auth.models import User
from test_liftit.models import Brand, Vehicle, VehicleType, Owner
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'email')


class VehicleTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleType
        fields = ('id', 'name', )


class VehicleSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    vehicle_type = VehicleTypeSerializer()

    class Meta:
        model = Vehicle
        fields = ('vehicle_plate', 'vehicle_type', 'owner')


class BrandSerializer(serializers.ModelSerializer):
    vehicles = VehicleSerializer(many=True)

    class Meta:
        model = Brand
        fields = ('name', 'count_vehicles', 'vehicles')
