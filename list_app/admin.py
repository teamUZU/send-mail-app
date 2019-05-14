from django.contrib import admin
from .models import Client
from .models import User

admin.site.register(Client)
admin.site.register(User)