from django.urls import path
from .views import login_view,logout_user,new_patient,results,view_results,patient_mgt
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('login/',login_view,name='login'),
    path('logout',logout_user,name='logout'),
    path('new/patient/',new_patient,name='new_patient'),
    path('results/<str:mrn>/',results,name='results'),
    path('view-results/<int:test_id>/<int:patient_id>/',view_results,name='view'),
    path('patient_mgt/',patient_mgt,name='patients')
]


# Password reset
urlpatterns+=[
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_management/reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_management/sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_management/new.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_management/done.html'),name='password_reset_complete'),
    
]