from django.contrib import admin

from .models import Director

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'bio')
    list_filter = ('title', )
    search_fields = ('name',)


admin.site.register(Director, DirectorAdmin)
