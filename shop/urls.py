from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#
# # May be not correct paths to files.
# urlpatterns += [
#      path('mainapp/', include('mainapp.urls')),
# ]
#
# urlpatterns += [
#     path('', RedirectView.as_view(url='/mainapp/', permanent=True)),
# ]
