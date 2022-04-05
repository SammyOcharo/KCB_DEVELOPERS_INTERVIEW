from django.db import models


class Account(models.Model):
    Account_Id = models.CharField(primary_key=True, unique=True, null=False, max_length=30)
    Iban = models.CharField(unique=True, max_length=30, null=False)
    bank_code = models.CharField(max_length=10)
    customer_id = models.CharField(max_length=10)


    def __str__(self):
        return self.Account_Id


class Card(models.Model):
    Card_account = models.ManyToOneRel(Account, field_name='card account', to=Account)
    Card_alias = models.CharField(max_length=20)
    Account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    Type_of_card = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.Card_account


