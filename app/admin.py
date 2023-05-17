from django.contrib import admin
from .models import recipe,recipe_card,Comment 

# Register your models here.

admin.site.register(recipe)
admin.site.register(recipe_card)
admin.site.register(Comment)
'''
from .models import BlogComment

admin.site.register(BlogComment)
'''