from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    # 1. Admin Panel
    path('admin/', admin.site.urls),
    
    # 2. Users App (Aapke purane saare functions yahan safe hain)
    path('users/', include('users_app.urls')),
    
    # 3. Home Redirect
    path('', lambda request: redirect('users/', permanent=False)),
]

# Media aur Static files ki purani settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)