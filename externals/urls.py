from .views import index,about,support
from django.urls import path


urlpatterns=[
    path('',index,name='home'),
    path('about/',about,name='about'),
    path('support/',support,name='support')
]