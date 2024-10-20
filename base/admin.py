from django.contrib import admin
from .models import Topics,Message,Rooms
# Register your models here.

admin.site.register(Topics)
admin.site.register(Message)
admin.site.register(Rooms)