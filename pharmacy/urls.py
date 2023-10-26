from django.urls import path
from .views import index,drug_stock

urlpatterns=[
    path('',index,name='pharm'),
    path('stock/',drug_stock,name='drugs')
]