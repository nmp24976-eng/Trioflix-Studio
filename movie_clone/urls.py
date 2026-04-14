from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    # 1. Admin Panel (Ye pehle se hai, isse rehne dein)
    path('admin/', admin.site.urls),
    
    # 2. Users App
    path('users/', include('users_app.urls')),
    
    # 3. Movies App (Ye line missing thi, isse movies load hongi)
    path('movies/', include('movies.urls')), 
    
    # 4. Home Redirect (Jab koi seedha website khole toh wo users/ par jaye)
    path('', lambda request: redirect('users/', permanent=False)),
]

# --- Sabse Zaroori Badlav (Media Files ke liye) ---
# Yahan se 'if settings.DEBUG' hata diya hai taaki Render par video chale
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)