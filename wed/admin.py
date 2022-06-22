
from django.contrib import admin
from .models import Category,Photo,Location,Profile
# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Location)
admin.site.register(Profile)
