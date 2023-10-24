from django.urls import path

from .views import patient_mgt,new_patient,results


urlpatterns=[
    path('',patient_mgt,name='patient_mgt'),
    path('new/',new_patient,name='new_patient'),
    path('view/<str:mrn>/',results,name='view')
]