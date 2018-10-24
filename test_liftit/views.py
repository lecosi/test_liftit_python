from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from test_liftit.models import Brand, Vehicle
from rest_framework import generics
from test_liftit.serializers import UserSerializer, BrandSerializer
from django.shortcuts import get_object_or_404, render
from test_liftit.forms import CreateVehicleForm, CreateOwnerForm
import csv


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        query = self.get_queryset()
        user = get_object_or_404(
            query,
            pk = self.kwargs['pk']
        )
        return user


def index(request):
    return render(request, 'base/base.html', {})


class BrandList(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)


def create_vehicle(request):
    form = CreateVehicleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Vehiculo creado')
        return HttpResponseRedirect('/create-vehicle/')

    return render(request, 'vehicle/register.html', {'form': form})


def create_owner(request):
    form = CreateOwnerForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Propietario creado')
        return HttpResponseRedirect('/create-owner/')

    return render(request, 'owner/register.html', {'form': form})


def generate_csv(request):
    if request.method == 'GET':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="report_vehicle.csv"'

        writer = csv.writer(response)
        writer.writerow(['placa', 'tipo', 'marca'])
        vehicles = Vehicle.objects.all()

        for vehicle in vehicles:
            writer.writerow([vehicle.vehicle_plate, vehicle.vehicle_type.name, vehicle.brand.name])

        return response


