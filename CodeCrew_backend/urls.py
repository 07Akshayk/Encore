from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('user/', include('users.urls'), name='users'),
    path('scholarship/', include('scholarship.urls'), name='scholarship'),
    path('events/', include('events.urls'), name='events'),
    
    path('overview/', views.apiOverview, name="api-urls")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)