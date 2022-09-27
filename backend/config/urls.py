from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
]
urlpatterns = [path('api/', include(urlpatterns)),]


if settings.PERFORMANCE_MODE_SILK:
    urlpatterns.append(path('silk/', include('silk.urls', namespace='silk')))

if settings.PERFORMANCE_MODE_DEBUG_TOOLBAR:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))


               
if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


