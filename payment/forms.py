from django import forms
from payment.models import  Paymentorder

class PaymentForm(forms.ModelForm):
     class Meta:
        model = Paymentorder
        fields = '__all__'


