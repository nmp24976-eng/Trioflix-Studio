from django.urls import path
from . import views

# Isse hum templates mein 'users_app:name' karke link kar sakte hain
# Jaise: {% url 'users_app:login' %}
app_name = 'users_app'

urlpatterns = [
    
    # ==========================================
    # 1. HOME & LANDING PAGES
    # ==========================================
    
    # Sabse pehla page (Landing Page)
    path('', views.index, name='index'),
    
    # FAQ (Sawal-Jawab) page ka rasta
    path('faq/', views.faq_view, name='faq_page'),
    
    # Help (Madat) page ka rasta
    path('help/', views.help_view, name='help_page'),


    # ==========================================
    # 2. AUTHENTICATION (Signup, Login, Logout)
    # ==========================================
    
    # Naya account banane ke liye (Registration)
    path('signup/', views.signup_view, name='signup'),
    
    # Website ke andar aane ke liye (Login)
    path('login/', views.my_login_view, name='login'),
    
    # Website se bahar nikalne ke liye (Logout)
    path('logout/', views.logout_view, name='logout'), 


    # ==========================================
    # 3. PROFILES & MEDIA CONTENT
    # ==========================================
    
    # Netflix style "Who's Watching?" screen ka rasta
    # Login ke turant baad user isi page par redirect hoga
    path('profiles/', views.profile_selection, name='profile_selection'),

    # Main Dashboard/Netflix Content jahan saari movies rows mein dikhengi
    path('media/', views.media_view, name='media'), 
    
    # User ki personal details dekhne wala page (User Profile)
    path('user/', views.user_detail_view, name='user_detail'),


    # ==========================================
    # 4. VIDEO PLAYER & WATCHLIST (My List) LOGIC
    # ==========================================

    # Specific movie play karne ke liye (movie_id ke saath)
    path('watch/<int:movie_id>/', views.watch_movie, name='watch_movie'),

    # NAYA FEATURE: Movie ko 'My List' mein Add ya Remove karne ke liye toggle logic
    # Is URL ko hum '+' button par use karenge
    path('watchlist/toggle/<int:movie_id>/', views.toggle_watchlist, name='toggle_watchlist'),
]