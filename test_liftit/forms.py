from django.contrib.auth.models import User
from django import forms
from test_liftit.models import Vehicle, Owner
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        labels = {
            'username': 'Nickname',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'password': 'Password',
        }


class CreateVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_plate', 'vehicle_type', 'brand', 'owner']


class CreateOwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'identification']