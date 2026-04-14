"""
Trioflix Studio - Final Production Settings
Cleaned & Optimized by Mohit Singh Negi
Permanent Database (Postgres) + Cloudinary Storage
"""

import os
import mimetypes
from pathlib import Path

# PostgreSQL ke liye smart URL handling library
try:
    import dj_database_url
except ImportError:
    dj_database_url = None

# --- 1. BASE DIRECTORY SETUP ---
BASE_DIR = Path(__file__).resolve().parent.parent

# Browser mein video files (MP4, M4V) ko sahi format mein play karne ke liye MIME types
mimetypes.add_type("video/mp4", ".m4v", True)
mimetypes.add_type("video/x-mp4", ".mp4", True)


# --- 2. SECURITY & DEBUG ---
SECRET_KEY = 'django-insecure-_ws5f9h!#%a185^k_ojt6@&r2fddfuiqxd8z%skd8r(leol4v-'

# LIVE SERVER PAR FALSE: Taaki errors na dikhein
DEBUG = False

# Render domain aur local testing ke liye hosts
ALLOWED_HOSTS = ['trioflix-studio.onrender.com', '.onrender.com', 'localhost', '127.0.0.1']

# CSRF SETTINGS: Render par Secure Login ke liye
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
    'whitenoise.middleware.WhiteNoiseMiddleware', # Static files (CSS) serve karne ke liye
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


# --- 4. DATABASE (Smart Switch: Postgres for Live, SQLite for Local) ---
# Agar Render par DATABASE_URL variable set hai, toh Postgres chalega
if dj_database_url and os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
else:
    # Local computer par purana SQLite hi chalta rahega
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# --- 5. STATIC & MEDIA FILES (Deployment Ready) ---
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Frontend folder ka path
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'users_app', 'frontend'),
]

# Whitenoise Storage settings
STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False # Taaki missing CSS file par crash na ho

# Media files
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
LOGIN_URL = 'users_app:login'
LOGIN_REDIRECT_URL = 'users_app:media'
LOGOUT_REDIRECT_URL = 'users_app:login'

# Default Primary Key type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'