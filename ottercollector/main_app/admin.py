from django.contrib import admin
from .models import Otter, Feeding, Toy

# Register your models here.
admin.site.register(Otter)
admin.site.register(Feeding)
admin.site.register(Toy)