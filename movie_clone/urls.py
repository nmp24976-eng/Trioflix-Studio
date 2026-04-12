"""
URL configuration for movie_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings             # <-- 1. Ye line add karein
from django.conf.urls.static import static   # <-- 2. Ye line add karein
from django.shortcuts import redirect  # <-- Yahan joda hai maine redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users_app.urls')),
    # Ye niche wali line aapki website kholte hi "users" par bhej degi
    path('', lambda request: redirect('users/', permanent=True)),
]

# --- Sabse zaruri hissa video seek karne ke liye ---
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
else:
    # Live server (Render) par bhi static files dikhne ke liye ye zaroori hai
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
