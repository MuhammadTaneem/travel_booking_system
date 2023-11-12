from django.contrib import admin


from .models import Booking


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Booking)
