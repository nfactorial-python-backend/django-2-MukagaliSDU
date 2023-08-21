from django.contrib import admin
from .models import News, Comments
# Register your models here.

# admin.site.register(News)
# admin.site.register(Comments)


class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 5


class AdminNews(admin.ModelAdmin):
    inlines = [CommentsInline]
    list_display = ["title", "content", "created_at", "has_comments"]


admin.site.register(News, AdminNews)
