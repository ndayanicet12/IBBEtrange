from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models

CURRENCY_CHOICES = (

    ('USD', 'USD'),
    ('EURO', 'EURO'),
)

ORDER_CHOICES = (
    ('BENEFICIAIRE', 'BENEFICIAIRE'),
    ('PRINCIPAL', 'PRINCIPAL'),
 
)

class Paymentorder(models.Model):
    monnaie = models.CharField(max_length=5, choices = CURRENCY_CHOICES,verbose_name=_(u'Monnaie'),default = "EURO")
    amountchiffre=models.FloatField(verbose_name=_(u' Montant en chiffres'))
    beneficiary = models.CharField(max_length=100,verbose_name=_(u'Beneficaire '))
    address = models.CharField(max_length=50, verbose_name=_(u'Adresse du beneficiaire'))
    bank = models.CharField(max_length=20, verbose_name=_(u'Banque'))
    accountbank= = models.CharField(max_length=20, verbose_name=_(u'Numero de Compte '))
    amountletter = models.CharField(max_length=256, verbose_name=_(u'Montant en lettres'))
    detailpayment = models.TextField(max_length=20, verbose_name=_(u'Detals de paiement'))
    datepayment = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Date'))
    principal  = models.CharField(max_length=50, verbose_name=_(u"Donneur d'ordre"))
    accountnumber = models.CharField(max_length=20, verbose_name=_(u'Numero de Compte'))
    ciostopay = models.CharField(max_length=20, choices = ORDER_CHOICES,verbose_name=_(u'Frais lies au transfert '),default = 'BENEFICIAIRE')




    def __str__(self):
           return self.monnaie


    class Meta:
         db_table = paymentorder
