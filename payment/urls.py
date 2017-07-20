from django.conf.urls import url

from . import views
 
app_name = 'payment'
urlpatterns = [        
	url(r'^$', views.CreatePayment.as_view(), name='createpayment'), 
	url(r'^index/$', views.ListPayment.as_view(), name='index'), 
	url(r'^addpayment/$', views.addpayment, name='addpayment'), 
<<<<<<< HEAD
 
=======
	url(r'^paymentdetail/(?P<pk>\d+)/$', views.DetailPayment.as_view(), name='paymentdetail'), 
>>>>>>> paymentdev
]
