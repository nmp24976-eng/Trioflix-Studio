from django.shortcuts import render
from .models import Movie  # Apne models se Movie class ko bulao

def index(request):
    # 1. Database se saari movies ko uthao
    movies_list = Movie.objects.all() 
    
    # 2. 'movies' naam ke key mein data ko HTML ko bhejo
    # HTML mein {% for movie in movies %} isi naam ki wajah se kaam karega
    return render(request, 'media.html', {'movies': movies_list})
