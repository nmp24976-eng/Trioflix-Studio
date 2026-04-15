"""
Trioflix Studio - Final Production Settings
Updated by Gemini for Mohit Singh Negi
Permanent Database (Supabase PostgreSQL) + Cloudinary Storage
"""

import os
import mimetypes 
from pathlib import Path

# --- 1. BASE DIRECTORY SETUP ---
BASE_DIR = Path(__file__).resolve().parent.parent

mimetypes.add_type("video/mp4", ".m4v", True)
mimetypes.add_type("video/x-mp4", ".mp4", True)

# --- 2. SECURITY & DEBUG ---
SECRET_KEY = 'django-insecure-_ws5f9h!#%a185^k_ojt6@&r2fddfuiqxd8z%skd8r(leol4v-'

# LIVE SERVER PAR FALSE: Render par True rakhne se security risk hota hai
DEBUG = False

ALLOWED_HOSTS = ['trioflix-studio.onrender.com', '.onrender.com', 'localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = ['https://trioflix-studio.onrender.com']

# --- 3. APPLICATION DEFINITION ---
INSTALLED_APPS = [
    'cloudinary_storage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'movies',
    'users_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'DIRS': [BASE_DIR / 'templates'],
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

# --- 4. DATABASE (Permanent Supabase Connection) ---
# Yahan humne SQLite hata kar Supabase (PostgreSQL) setup kar diya hai.
# --- 4. DATABASE (Manual Supabase Connection) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'MohitTrioflix2026', 
        'HOST': 'db.cbsprplyznawovoapzuv.supabase.co',
        'PORT': '5432',
    }
}
# --- 5. STATIC & MEDIA FILES ---
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'users_app', 'frontend'),
]

STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- 6. CLOUDINARY CONFIGURATION ---
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dxphyzpeg',
    'API_KEY': '829991893926926',
    'API_SECRET': '_Q7liYV74wkn8C8cNVrwWZCVPBM',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# --- 7. AUTHENTICATION & REDIRECTS ---
LOGIN_URL = 'users_app:login'
LOGIN_REDIRECT_URL = 'users_app:media'
LOGOUT_REDIRECT_URL = 'users_app:login'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'