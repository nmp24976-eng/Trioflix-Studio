"""
WSGI config for movie_clone project.
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise # <--- Ye line add karni hai

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_clone.settings')

application = get_wsgi_application()

# Render par CSS chalane ke liye ye sabse zaroori line hai
application = WhiteNoise(application)