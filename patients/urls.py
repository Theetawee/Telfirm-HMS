from django.urls import path

from .views import new_patient,view_patient,view_results,see_results,confirm_results,print_results


urlpatterns=[
    path('new/',new_patient,name='new_patient'),
    path('view/<str:mrn>/',view_patient,name='view'),
    path('results/<int:test_id>/<int:patient_id>/',view_results,name='results'),
    path('view/results/<int:test_id>/<int:patient_id>/',see_results,name='view_results'),
    path('confirm_results/<int:test_id>/<int:patient_id>/',confirm_results,name='confirm_results'),
    path('print_results/<int:test_id>/<int:patient_id>/',print_results,name='print_results'),
]