
from django.urls import path
from users_app import views  # Seedha users_app ke views uthao

app_name = 'movies' # Isse Django ko pata chalta hai ki ye movies app hai

urlpatterns = [
    # Ye wo link hai jo video player ko kholega
    path('watch/<int:movie_id>/',views.watch_movie, name='watch_movie'),
]