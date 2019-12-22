from django.contrib import admin

from .models import Title,Article

# Register your models here.

admin.site.site_header = "Tray Admin"
admin.site.site_title = "Tray Admin Area"
admin.site.index_title = "Welcome to the Tray admin area"

class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0


class TitleAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title_text']}),
                 (None, {'fields' : ['likes']}),
                 ('Date Information', {'fields': ['pub_date'],  'classes': ['collapse']}), ]
    inlines = [ArticleInline]


admin.site.register(Title,TitleAdmin)