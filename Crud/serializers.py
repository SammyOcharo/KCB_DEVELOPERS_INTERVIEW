from django.db.models import fields
from rest_framework import serializers
from .models import Account, Card


#rest framework serializers help in convetion of json data into python readable files for storage
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model= Account
        fields = ('Account_Id', 'Iban', 'bank_code', 'customer_id')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields = ('Card_account',
                    'Card_alias',
                    'Account_id',
                    'Type_of_card')