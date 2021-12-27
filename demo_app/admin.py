from django.contrib import admin

from demo_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
