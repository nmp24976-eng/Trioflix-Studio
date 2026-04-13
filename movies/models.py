from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings # User model ko link karne ke liye

# 1. Category Model (Movies ko classify karne ke liye)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. Movie Model (Aapka existing model + thode sudhar)
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # Content Type (Film, Series etc.)
    TYPE_CHOICES = [
        ('movie', 'Film'),
        ('series', 'Web Series'),
        ('documentary', 'Documentary'),
        ('kids', 'Kids Content'), # Naya: Kids section ke liye
    ]
    content_type = models.CharField(
        max_length=20, 
        choices=TYPE_CHOICES, 
        default='movie',
        help_text="Select karein ki ye Film hai, Series ya Documentary"
    )

    # --- POSTER SECTION ---
    poster_url = models.URLField(max_length=1000, blank=True, null=True, help_text="Direct Image Link dalo")
    poster_file = CloudinaryField('image', folder='posters', blank=True, null=True)

    # --- VIDEO SECTION ---
    youtube_url = models.URLField(max_length=1000, null=True, blank=True, help_text="YouTube Watch link dalo")
    video_file = CloudinaryField('video', resource_type='video', folder='movies', blank=True, null=True)
    # Naya Field Yahan Add Karein:
    video_url = models.URLField(max_length=1000, null=True, blank=True, help_text="Cloudinary ka direct video link yahan dalo")
    
    # Categories: Ek movie ki kai categories ho sakti hain (e.g. Action + Trending)
    categories = models.ManyToManyField(Category, related_name='movies')

    def __str__(self):
        return f"{self.title} ({self.get_content_type_display()})"

# ==========================================
# 3. NAYA MODEL: WATCHLIST (My List Feature)
# ==========================================
class Watchlist(models.Model):
    # 'user' connect karega ki kisne save kiya hai
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_watchlist')
    
    # 'movie' connect karega ki kaunsi film save hui hai
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    # Kab add kiya gaya
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Isse ek user ek movie ko sirf ek baar save kar payega (Duplicate nahi hoga)
        unique_together = ('user', 'movie')
        ordering = ['-added_on'] # Latest saved movie pehle dikhegi

    def __str__(self):
        return f"{self.user.username} ki list - {self.movie.title}"