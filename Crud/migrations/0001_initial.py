# Generated by Django 4.0.3 on 2022-04-05 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('Account_Id', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('Iban', models.CharField(max_length=30, unique=True)),
                ('bank_code', models.CharField(max_length=10)),
                ('customer_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Card_account', models.CharField(max_length=20, unique=True)),
                ('Card_alias', models.CharField(max_length=20)),
                ('Type_of_card', models.CharField(max_length=10)),
                ('Account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Crud.account')),
            ],
        ),
    ]
