from django.contrib import admin
from .models import CustomUser


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, AuthorAdmin)
