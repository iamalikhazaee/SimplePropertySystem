from rest_framework import serializers
from .models import *
from django.shortcuts import render
from django.http import HttpResponse

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['title']

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['firstname','lastname']

class ProfileSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    class Meta:
        model = Profile
        fields = ['firstname','lastname','username','national_code','refer_code','phone','role']

class SellContractSerializer(serializers.ModelSerializer):
    buyer = NameSerializer()
    seller = NameSerializer()
    expert = NameSerializer()
    class Meta:
        model = sell_Contract
        fields = ['id', 'buyer', 'seller', 'expert', 'status', 'property','tracking_code']

class RentContractSerializer(serializers.ModelSerializer):
    owner = NameSerializer()
    renter = NameSerializer()
    expert = NameSerializer()
    class Meta:
        model = rent_Contract
        fields = ['id', 'renter', 'owner', 'expert', 'status', 'property','tracking_code']

class SellPropertySerializer(serializers.ModelSerializer):
    owner = NameSerializer()
    class Meta:
        model = sell_Property
        fields = ['owner', 'meterage', 'construction_year', 'neighborhood_name', 'parking', 'sell_price','approve']

class RentPropertySerializer(serializers.ModelSerializer):
    owner = NameSerializer()
    class Meta:
        model = rent_Property
        fields = ['owner', 'meterage', 'construction_year', 'neighborhood_name', 'parking','rent_price','deposit','approve']




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'