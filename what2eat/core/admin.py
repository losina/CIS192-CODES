from django.contrib import admin
from core.models import List, Restaurant, Category, CategoryList


admin.site.register(List)
admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(CategoryList)

