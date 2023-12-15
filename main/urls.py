from django.urls import path
from .views import search,create_notice,view_notice,view_notice_detail,close_notice,mark_read




urlpatterns=[
    path('search',search,name='search'),
    path('create_notice',create_notice,name='create_notice'),
    path('view_notice',view_notice,name='view_notice'),
    path('view_notice/<int:pk>',view_notice_detail,name='detail'),
    path('close_notice/<int:pk>',close_notice,name='close_notice'),
    path('mark_read/<int:pk>',mark_read,name='mark_read')
]












