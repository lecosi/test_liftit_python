"""test_liftit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from test_liftit.views import UserList, index, BrandList, create_vehicle, create_owner, generate_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='local'),
    path('user_list/', csrf_exempt(UserList.as_view()), name='user_list'),
    path('create-vehicle/', create_vehicle, name='create_vehicle'),
    path('brand-list/', BrandList.as_view(), name='brand_list'),
    path('create-owner/', create_owner, name='create_owner'),
    path('generate-csv/', generate_csv, name='generate_csv'),
]
