from django.urls import path
from .views import drug_stock

urlpatterns=[
    path('stock/',drug_stock,name='drugs')
]