from django.contrib import admin
from .models import GAAClub, UserProfile, Player, Author, Book

admin.site.register(GAAClub)
admin.site.register(UserProfile)
admin.site.register(Player)
admin.site.register(Author)
admin.site.register(Book)