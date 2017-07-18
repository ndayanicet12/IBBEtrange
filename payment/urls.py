from django.conf.urls import url

from . import views
 
app_name = 'payment'
urlpatterns = [        
	url(r'^$', views.CreatePayment.as_view(), name='createpayment'), 
]
