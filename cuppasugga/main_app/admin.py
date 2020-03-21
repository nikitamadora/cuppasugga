from django.contrib import admin
from .models import Profile, Bag, Item

# Register your models here.
admin.site.register(Profile)
admin.site.register(Bag)
admin.site.register(Item)