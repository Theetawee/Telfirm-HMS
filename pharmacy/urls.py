from django.urls import path
from .views import prescribe_drug,drug_stock

urlpatterns=[
    path('<str:patient_id>/',prescribe_drug,name='pharm'),
    path('stock/',drug_stock,name='drugs')
]