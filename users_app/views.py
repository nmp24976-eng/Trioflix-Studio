from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Naya Import: Watchlist model ko zaroor add karein
from movies.models import Movie, Category, Watchlist 

# ==========================================
# 1. LANDING & STATIC PAGES (Bina Login wale)
# ==========================================

# Index Page: Landing page jahan sabse pehle user aata hai
def index(request):
    all_movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': all_movies})

# FAQ Page: Sawal-Jawab section
def faq_view(request): 
    return render(request, 'FAQ.html')

# Help Page: Support ke liye
def help_view(request): 
    return render(request, 'help.html')


# ==========================================
# 2. AUTHENTICATION (Login, Signup, Logout)
# ==========================================

# Signup Logic: Naya user register karne ke liye
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users_app:profile_selection')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login Logic: Purane user ke liye
def my_login_view(request):
    if request.user.is_authenticated:
        return redirect('users_app:profile_selection') 
        
    if request.method == 'POST':
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')
        user = authenticate(request, username=u_name, password=p_word)
        
        if user:
            login(request, user)
            return redirect('users_app:profile_selection') 
        else:
            messages.error(request, 'Invalid Username or Password!')
            
    return render(request, 'signin.html')

# Profile Selection: "Who's Watching?" wali screen
@login_required
def profile_selection(request):
    return render(request, 'profiles.html')

# Logout: Bahar nikalne ke liye
def logout_view(request): 
    logout(request)
    return redirect('users_app:login')


# ==========================================
# 3. USER & MEDIA CONTENT (Login Zaroori Hai)
# ==========================================

# User Profile: Personal details page
@login_required
def user_detail_view(request):
    return render(request, 'user.html', {'user': request.user})

# ==========================================
# 2. MEDIA CENTER (Fixed Category Logic)
# ==========================================

@login_required
def media_view(request):
    search_query = request.GET.get('q') 
    all_categories = Category.objects.all()
    
    # FIX 1: User ki personal "My List" nikalna (Ye context mein missing tha)
    my_list_items = Watchlist.objects.filter(user=request.user)
    my_list_movies = [item.movie for item in my_list_items]

    # FIX 2: Shared List Bug hata diya (Har category ko alag-alag rakha hai)
    # Python mein a = b = [] likhne se data clash hota tha
    movies = []
    trending, action, drama, crime = [], [], [], []
    series, documentary, kids, reality = [], [], [], []
    search_mode = False

    if search_query:
        movies = Movie.objects.filter(title__icontains=search_query)
        search_mode = True
    else:
        # FIX 3: .distinct() add kiya taaki data repeat na ho
        trending = Movie.objects.filter(content_type='movie', categories__name__icontains='Trending').distinct()
        action = Movie.objects.filter(content_type='movie', categories__name__icontains='Action').distinct()
        drama = Movie.objects.filter(content_type='movie', categories__name__icontains='Drama').distinct()
        crime = Movie.objects.filter(content_type='movie', categories__name__icontains='Crime').distinct()
        
        series = Movie.objects.filter(content_type='series').distinct()
        documentary = Movie.objects.filter(content_type='documentary').distinct()
        kids = Movie.objects.filter(content_type='kids').distinct()
        reality = Movie.objects.filter(content_type='reality').distinct()

    context = {
        'movies': movies,
        'trending': trending, 'action': action, 'drama': drama, 'crime': crime,
        'series': series, 'documentary': documentary, 'kids': kids, 'reality': reality,
        'all_categories': all_categories,
        'search_mode': search_mode,
        'my_list': my_list_movies, # FIX: watchlist movies template ko bheji
    }
    return render(request, 'media.html', context)

# ... (toggle_watchlist aur watch_movie functions yahan pehle jaise hi rahenge) ...

# ==========================================
# 4. WATCHLIST LOGIC (My List Feature)
# ==========================================

@login_required
def toggle_watchlist(request, movie_id):
    """Movie ko list mein Add ya Remove karne ka logic"""
    movie = get_object_or_404(Movie, id=movie_id)
    watchlist_item = Watchlist.objects.filter(user=request.user, movie=movie)

    if watchlist_item.exists():
        watchlist_item.delete()
        messages.info(request, f"{movie.title} removed from My List.")
    else:
        Watchlist.objects.create(user=request.user, movie=movie)
        messages.success(request, f"{movie.title} added to My List.")

    # User ko wapas usi page par bhejo jahan wo tha
    return redirect(request.META.get('HTTP_REFERER', 'users_app:media'))


# ==========================================
# 5. VIDEO PLAYER LOGIC (YouTube + Cloudinary)
# ==========================================

@login_required
def watch_movie(request, movie_id):
    # 1. Movie dhoondo, nahi mile toh 404 error
    movie_data = get_object_or_404(Movie, id=movie_id)
    video_url = ""

    # 2. Check karein (Dhyan dein: aapke model mein jo naam hai wahi likhein)
    # Agar model mein field 'video_url' hai toh wahi use karein
    if hasattr(movie_data, 'video_url') and movie_data.video_url:
        video_url = movie_data.video_url
    elif hasattr(movie_data, 'youtube_url') and movie_data.youtube_url:
        video_url = movie_data.youtube_url
    elif movie_data.video_file:
        video_url = movie_data.video_file.url

    # 3. Agar kuch nahi mila toh wapas bhej do aur error dikhao
    if not video_url:
        messages.error(request, "Video link available nahi hai!")
        return redirect('users_app:media')

    # 4. YouTube Link Conversion Logic (Fixed)
    if "youtube.com/watch?v=" in video_url:
        video_url = video_url.replace("youtube.com/watch?v=", "www.youtube-nocookie.com/embed/")
    elif "youtu.be/" in video_url:
        video_url = video_url.replace("youtu.be/", "www.youtube-nocookie.com/embed/")

    # 5. Clean up URL
    if "embed" in video_url:
        # Extra parameters hatayein taaki clean link mile
        video_url = video_url.split("&")[0].split("?")[0] + "?rel=0&modestbranding=1&autoplay=1"

    # 6. Render: Yahan file ka naam check karein (watch.html ya media.html)
    return render(request, 'media.html', {
        'movie': movie_data, 
        'final_url': video_url,
        'is_watching': True # Template mein handle karne ke liye
    })