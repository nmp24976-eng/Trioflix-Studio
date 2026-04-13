"""
Trioflix Studio - Final Production Settings
Cleaned & Optimized by Mohit Singh Negi
"""

import os
import mimetypes
from pathlib import Path

# --- 1. BASE DIRECTORY SETUP ---
# Project ki main root directory ka path nikalne ke liye
BASE_DIR = Path(__file__).resolve().parent.parent

# Browser mein video files (MP4, M4V) ko sahi format mein play karne ke liye MIME types
mimetypes.add_type("video/mp4", ".m4v", True)
mimetypes.add_type("video/x-mp4", ".mp4", True)


# --- 2. SECURITY & DEBUG ---
# SECRET_KEY ko safe rakhein (Production mein ise environment variable se lena chahiye)
SECRET_KEY = 'django-insecure-_ws5f9h!#%a185^k_ojt6@&r2fddfuiqxd8z%skd8r(leol4v-'

# LIVE SERVER PAR FALSE HONA CHAHIYE: Taaki users ko errors na dikhein
DEBUG = False

# Render domain, subdomains aur local testing ke liye hosts ko allow karna
ALLOWED_HOSTS = ['trioflix-studio.onrender.com', '.onrender.com', 'localhost', '127.0.0.1']

# CSRF SETTINGS: Render par Secure Login ke liye ye line sabse zaroori hai
CSRF_TRUSTED_ORIGINS = ['https://trioflix-studio.onrender.com']


# --- 3. APPLICATION DEFINITION ---
INSTALLED_APPS = [
    'cloudinary_storage',         # Cloudinary storage handling (Top par hona zaroori hai)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # CSS/JS handle karne ke liye
    'cloudinary',                 # Cloudinary main library
    'movies',                     # Movies App
    'users_app',                  # Users/Auth App
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Render par Static files (CSS) serve karne ke liye No. 1 Middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'movie_clone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Global templates folder ka rasta
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


# --- 4. DATABASE (SQLite) ---
# Production ke liye SQLite use ho raha hai (Simple setup)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --- 5. STATIC & MEDIA FILES (Deployment Ready) ---
# Static files (CSS, JS, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Frontend folder ka path check karein (Agar folder ka naam 'static' hai toh wahi likhein)
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'users_app', 'frontend'),
]

# Whitenoise Storage: Static files ko bina crash ke fast serve karta hai
STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'
WHITENOISE_USE_FINDERS = True

# Media files: User jo poster ya video upload karega
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# --- 6. CLOUDINARY FINAL CONFIGURATION ---
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

# Media files ko default Cloudinary par save karne ke liye
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# --- 7. AUTHENTICATION & REDIRECTS ---
# Login aur Logout ke baad user kahan jayega
LOGIN_URL = 'users_app:login'
LOGIN_REDIRECT_URL = 'users_app:media'
LOGOUT_REDIRECT_URL = 'users_app:login'

# Default Primary Key type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'