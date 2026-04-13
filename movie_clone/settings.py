"""
Django settings for movie_clone project.
Cleaned, Organized & Deployment Ready by Mohit Singh Negi
"""

import os
import mimetypes
from pathlib import Path

# Video files ko browser mein sahi se dikhane ke liye mime-types
mimetypes.add_type("video/mp4", ".m4v", True)
mimetypes.add_type("video/x-mp4", ".mp4", True)

# Project ki main directory ka path
BASE_DIR = Path(__file__).resolve().parent.parent

# --- 1. Security & Debug ---
SECRET_KEY = 'django-insecure-_ws5f9h!#%a185^k_ojt6@&r2fddfuiqxd8z%skd8r(leol4v-'

# DEPLOYMENT TIP: Live server par ise False kar dein
DEBUG = False

# Ismein '*' ka matlab hai ki koi bhi host ise access kar sakta hai (Deployment ke liye zaroori)
ALLOWED_HOSTS = ['trioflix-studio.onrender.com', '127.0.0.1', 'localhost']


# --- 2. Application Definition ---
INSTALLED_APPS = [
    'cloudinary_storage',         # Sabse upar zaroori hai
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
    'whitenoise.middleware.WhiteNoiseMiddleware', # NAYA: Static files ko server par bina crash ke chalane ke liye
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

# --- 3. Database (SQLite Configuration) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --- 4. Password Validation ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- 5. Internationalization ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- 6. Static & Media Files (Deployment Config) ---
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # NAYA: Live server ke liye files jama karne ki jagah

# Is line ko dhyaan se dekhein, shayad 'movie_clone' folder ki wajah se BASE_DIR ek level peeche hai
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend'),
]
# NAYA: Whitenoise storage taaki CSS/JS compress hokar chale
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
WHITENOISE_USE_FINDERS = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# --- 7. Login & Redirect Settings ---
LOGIN_URL = 'users_app:login'
LOGIN_REDIRECT_URL = 'users_app:media'
LOGOUT_REDIRECT_URL = 'users_app:login'


# --- 8. Cloudinary Final Configuration ---
import cloudinary
import cloudinary.uploader
import cloudinary.api

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dxphyzpeg',
    'API_KEY': '829991893926926',
    'API_SECRET': '_Q7liYV74wkn8C8cNVrwWZCVPBM',
}

cloudinary.config( 
    cloud_name = "dxphyzpeg", 
    api_key = "829991893926926", 
    api_secret = "_Q7liYV74wkn8C8cNVrwWZCVPBM",
    secure = True
)

# Images aur videos ko Cloudinary par bhejta hai
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'