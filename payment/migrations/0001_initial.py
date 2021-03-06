# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-19 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paymentorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monnaie', models.CharField(choices=[('USD', 'USD'), ('EURO', 'EURO')], default='EURO', max_length=5, verbose_name='Monnaie')),
                ('amountchiffre', models.FloatField(verbose_name=' Montant en chiffres')),
                ('beneficiary', models.CharField(max_length=256, verbose_name='Beneficaire ')),
                ('address', models.TextField(max_length=256, verbose_name='Adresse du beneficiaire')),
                ('bank', models.CharField(max_length=256, verbose_name='Banque')),
                ('accountbank', models.CharField(max_length=256, verbose_name='Numero de Compte ')),
                ('ibancode', models.CharField(max_length=256, verbose_name=' Code Iban   ')),
                ('swiftcode', models.CharField(max_length=256, verbose_name='Code SWIFT')),
                ('addressbank', models.TextField(max_length=256, verbose_name='Adresse de la Banque')),
                ('amountletter', models.CharField(max_length=256, verbose_name='Montant en lettres')),
                ('detailpayment', models.TextField(max_length=256, verbose_name='Detals de paiement')),
                ('datepayment', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('principal', models.CharField(max_length=256, verbose_name="Donneur d'ordre")),
                ('accountnumber', models.CharField(max_length=20, verbose_name='Numero de Compte')),
                ('ciostopay', models.CharField(choices=[('BENEFICIAIRE', 'BENEFICIAIRE'), ('PRINCIPAL', 'PRINCIPAL')], default='BENEFICIAIRE', max_length=20, verbose_name='Frais lies au transfert ')),
            ],
            options={
                'db_table': 'paymentorder',
            },
        ),
    ]
