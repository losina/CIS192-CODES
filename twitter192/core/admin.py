from django.contrib import admin
from core.models import Tweet, HashTag, Like

# Register your models here.
admin.site.register(Tweet)
admin.site.register(HashTag)
admin.site.register(Like)