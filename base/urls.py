from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),     
    path('',include('main.urls')),
    path('accounts/',include('accounts.urls')),
    path('patients/',include('patients.urls')),
    path('pharmacy/',include('pharmacy.urls')),
    path('doctor/',include('doctor.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'main.utils.custom_404_view'
handler400 = 'main.utils.custom_404_view'
handler500 = 'main.utils.custom_500_view'
handler403 = 'main.utils.custom_404_view'

admin.site.site_header='Telfirm'
admin.site.site_title='Telfirm Admin'
admin.site.index_title='Welcome to the Telfirm Admin Panel'