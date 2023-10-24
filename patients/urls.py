from django.urls import path

from .views import patient_mgt


urlpatterns=[
    path('',patient_mgt,name='patient_mgt')
]