from django.contrib import admin
from .models import NeighbourHood, UserProfile, Business, Location, Post, Comment

admin.site.register(NeighbourHood)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Comment)
