from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from payment.forms import * 
from payment.models import *

class CreatePayment(CreateView):
    model=Paymentorder
    form_class=PaymentForm
    template_name='payment/createpayment.html'
    context_object_name = "payment"
    
    def get_object(self):
 
       return super(CreateTransfer, self).get_object()

    
 
    def get_success_url(self):
        return reverse('payment:index')

    def get_context_data(self, **kwargs):
        context = super(CreatePayment, self).get_context_data(**kwargs)
        context['action'] = reverse('payment:index')
        return context

class ListPayment(ListView):
    model=Paymentorder
    form_class=PaymentForm
    template_name='payment/index.html'
    context_object_name = "payment"
    
    def get_queryset(self):
       return Paymentorder.objects.all().order_by('-amountchiffre')

    def get_success_url(self):
        return reverse('payment:index')

    def get_context_data(self, **kwargs):
        context = super(ListPayment, self).get_context_data(**kwargs)
        context['action'] = reverse('payment:index')
        return context



