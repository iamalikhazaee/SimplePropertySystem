from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from App import serializers

from random import randint, randrange

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = serializers.RoleSerializer

class SellContractViewSet(viewsets.ModelViewSet):
    queryset = sell_Contract.objects.all()
    serializer_class = serializers.SellContractSerializer

    @action(detail= True ,name = 'Final Agreement')
    def changing_state(self, request, pk=None):
        contract = sell_Contract.objects.get(id = pk)
        contract.status = 'final agreement'
        contract.tracking_code = str(randrange(1000000000, 10000000000))
        contract.save()
        return Response(serializers.SellContractSerializer(contract).data)

class RentContractViewSet(viewsets.ModelViewSet):
    queryset = rent_Contract.objects.all()
    serializer_class = serializers.RentContractSerializer

    @action(detail= True,name = 'Final Agreement')
    def changing_state(self, request, pk=None):
        contract = rent_Contract.objects.get(id = pk)
        contract.status = 'final agreement'
        contract.tracking_code = str(randrange(1000000000, 10000000000))
        contract.save()
        return Response(serializers.RentContractSerializer(contract).data)


class SellPropertyViewSet(viewsets.ModelViewSet):
    queryset = sell_Property.objects.all()
    serializer_class = serializers.SellPropertySerializer

class RentPropertyViewSet(viewsets.ModelViewSet):
    queryset = rent_Property.objects.all()
    serializer_class = serializers.RentPropertySerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = serializers.CustomerSerializer