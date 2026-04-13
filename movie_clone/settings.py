"""
Django settings for Trioflix Studio (Movie Clone).
Developed & Maintained by: Mohit Singh Negi
"""

import os
import mimetypes
from pathlib import Path

# --- BASE DIRECTORY SETUP ---
# Ye line batati hai ki project ka main folder kahan hai
BASE_DIR = Path(__file__).resolve().parent.parent

# Browser mein video files (MP4) ko sahi format mein play karne ke liye settings
mimetypes.add_type("video/mp4", ".m4v", True)
mimetypes.add_type("video/x-mp4", ".mp4", True)


# --- 1. SECURITY & DEBUG ---
SECRET_KEY = 'django-insecure-_ws5f9h!#%a185^k_ojt6@&r2fddfuiqxd8z%skd8r(leol4v-'

# PRODUCTION TIP: Render par deploy karte waqt ise False rakhein taaki koi error leak na ho
DEBUG = False

# Render ki URL aur local URLs ko allow karna zaroori hai
# Ise bilkul aisa kar dein
ALLOWED_HOSTS = ['trioflix-studio.onrender.com', '.onrender.com', 'localhost', '127.0.0.1']
# --- CSRF Fix (Iske bina Login nahi hoga) ---
# Ye line Django ko batati hai ki Render se aane wala login request safe hai
CSRF_TRUSTED_ORIGINS = ['https://trioflix-studio.onrender.com']



# --- 2. INSTALLED APPLICATIONS ---
INSTALLED_APPS = [
    'cloudinary_storage',         # Cloudinary storage handling (Sabse upar hona chahiye)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # Static files (CSS/JS) handle karne ke liye
    'cloudinary',                 # Cloudinary main library
    'movies',                     # Aapka Movies app
    'users_app',                  # Aapka User/Login app
]


# --- 3. MIDDLEWARE CONFIGURATION ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # IMPORTANT: Render par CSS/JS serve karne ke liye
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'movie_clone.urls'


# --- 4. TEMPLATE SETTINGS ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # HTML files dhoondne ka rasta
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'movie_clone.wsgi.application'


# --- 5. DATABASE (SQLite) ---
# Mohit, abhi hum SQLite use kar rahe hain jo local testing ke liye best hai
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --- 6. STATIC & MEDIA FILES (Whitenoise & Cloudinary) ---
# Static files (CSS, Images, JS)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Frontend folder ka path dhyan se check karein (Agar folder ka naam 'static' hai toh badal dein)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend'), 
]

# Whitenoise settings: CSS ko compress karke fast load karta hai
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_USE_FINDERS = True

# Media files (User jo video/photo upload karega)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# --- 7. CLOUDINARY CONFIGURATION ---
# Ye settings aapke images aur videos ko Cloudinary par store karengi
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dxphyzpeg',
    'API_KEY': '829991893926926',
    'API_SECRET': '_Q7liYV74wkn8C8cNVrwWZCVPBM',
}

import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( 
    cloud_name = "dxphyzpeg", 
    api_key = "829991893926926", 
    api_secret = "_Q7liYV74wkn8C8cNVrwWZCVPBM",
    secure = True
)

# Media files ko default Cloudinary par bhejta hai
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# --- 8. LOGIN & AUTH SETTINGS ---
# Login hone ke baad user kahan jayega?
LOGIN_URL = 'users_app:login'
LOGIN_REDIRECT_URL = 'users_app:media'
LOGOUT_REDIRECT_URL = 'users_app:login'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'