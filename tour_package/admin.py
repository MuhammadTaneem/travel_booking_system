from django.contrib import admin


from .models import TourPackage


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(TourPackage, AuthorAdmin)