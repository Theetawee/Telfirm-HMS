from django.urls import path
from .views import index,prescribe_drug


urlpatterns=[
    path('',index,name='doctor'),
    path('prescription/<int:patient_id>/',prescribe_drug,name='pres')    
]