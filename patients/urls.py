from django.urls import path

from .views import new_patient,view_patient,view_results,patientsList,load_p


urlpatterns=[
    path('',patientsList,name='patient_mgt'),
    path('new/',new_patient,name='new_patient'),
    path('view/<str:mrn>/',view_patient,name='view'),
    path('results/<int:test_id>/<int:patient_id>/',view_results,name='results'),
    path('load_patients/',load_p,name='load')
]