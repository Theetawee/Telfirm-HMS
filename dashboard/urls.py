from django.urls import path
from .views import dashboard_view,search_view,load_patients,load_patients_page



urlpatterns=[
    path('',dashboard_view,name='dashboard'),
    path('search/',search_view,name='search'),
    path('load/patients/',load_patients,name='load_patients'),
    path('load/patients/more/',load_patients_page,name='load_more')
]