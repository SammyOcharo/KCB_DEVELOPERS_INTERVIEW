from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AccountSerializer, CardSerializer
from .models import Account, Card
from rest_framework import serializers

@api_view(['GET'])
def AllCards(request):
    if request.query_params:
        items = Account.objects.filter(**request.query_param.dict())

    else:
        items = Account.objects.all()

    if items:
        data = AccountSerializer(items)

        return Response(data)
    else:

        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_Card_details(request):
    item = CardSerializer(data=request.data)

    if Card.objects.filter(**request.data).exists():
        raise serializers.ValidationError("Card number already exists")

    if item.is_valid():
        item.save()
        return Response(item.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def account_update(request, pk):
    item = Account.objects.get(pk=pk)

    data = AccountSerializer(instance= item, data=request.data)

    if data.is_valid():
        data.save()

        return Response(data.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def account_delete(request, pk):
    item = get_object_or_404(Account, pk=pk)

    item.delete()

    return Response(status=status.HTTP_202_ACCEPTED)