from django.db import models
from builtins import property


class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    identification = models.FileField(upload_to='upload/', blank=True, null=True)
    id_number = models.CharField(max_length=11, unique=True, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.first_name

    def as_json(self):
        payload = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone_number,
        }
        return payload

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = ('%s %s' % (self.first_name, self.last_name)).upper()
        return full_name.strip()


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def count_vehicles(self):
        return self.vehicles.count()


class VehicleType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_plate = models.CharField(max_length=10, unique=True)
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='vehicles')
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.vehicle_plate
