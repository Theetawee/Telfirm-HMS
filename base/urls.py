from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from .utils import service_worker, manifest, RobotsTxtView,offline


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("externals.urls")),
    path("accounts/", include("accounts.urls")),
    path("patients/", include("patients.urls")),
    path("pharmacy/", include("pharmacy.urls")),
    path("doctor/", include("doctor.urls")),
    path('dashboard/',include('dashboard.urls')),
    path('',include('main.urls'))
]


urlpatterns += [
    re_path(r"^serviceworker\.js$", service_worker, name="sw"),
    re_path(r"^manifest\.json$", manifest, name="manifest"),
    path("offline/", offline, name="offline"),
    re_path(r"^robots\.txt$", RobotsTxtView.as_view()),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = "base.utils.custom_404_view"
handler400 = "base.utils.custom_404_view"
handler500 = "base.utils.custom_500_view"
handler403 = "base.utils.custom_404_view"

admin.site.site_header = "Telfirm"
admin.site.site_title = "Telfirm Admin"
admin.site.index_title = "Welcome to the Telfirm Admin Panel"
