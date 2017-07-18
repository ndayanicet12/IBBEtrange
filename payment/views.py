from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from payment.forms import * 
from payment.models import *

class CreatePayment(CreateView):
    model=Paymentorder
    #fields = "__all__"
    form_class=PaymentForm
    template_name='payment/createpayment.html'
    #context_object_name = "payment"
    
    def get_object(self):
 
       return super(CreatePayment, self).get_object()

    
 
    def get_success_url(self):
        return reverse('payment:index')

    def get_context_data(self, **kwargs):
        context = super(CreatePayment, self).get_context_data(**kwargs)
        context['action'] = reverse('payment:index')
        return context

class ListPayment(ListView):
    model=Paymentorder
    #form_class=PaymentForm
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


def  addpayment(request):
	 
    if request.method=='POST':
  
        trs = Paymentorder.objects.create( monnaie=request.POST['monnaie'], amountchiffre=request.POST['amountchiffre'],beneficiary=request.POST['beneficiary'], address=request.POST['address'], bank=request.POST['bank'],accountbank = request.POST['accountbank'], amountletter=request.POST['amountletter'], detailpayment=request.POST['detailpayment'], principal=request.POST['principal'], accountnumber=request.POST['accountnumber'],ciostopay=request.POST['ciostopay'])
        trs.save()
	return render(request, 'payment/addpayment.html', {'trs':trs})
                  
    else:
        form=PaymentForm()
        return render(request, 'payment/addpayment.html', {'form':form})



