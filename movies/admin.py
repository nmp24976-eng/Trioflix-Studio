from django.contrib import admin
from .models import Movie, Category

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',) # Isse categories select karna bahut easy ho jayega

admin.site.register(Category)