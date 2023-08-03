from django.contrib import admin
from . models import Users, Message, Items

# Register your models here.

admin.site.register(Users)
admin.site.register(Message)
admin.site.register(Items)
