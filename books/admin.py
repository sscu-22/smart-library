from django.contrib import admin
from .models import Book, Bookmark, Category, ReadingHistory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "code_number",
        "language",
        "published_year",
        "available_copies",
        "views_count",
    )
    list_filter = ("category", "language", "published_year")
    search_fields = ("title", "author", "code_number", "tags")
    readonly_fields = ("views_count", "created_at")


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "created_at")
    search_fields = ("user__username", "book__title")
    list_filter = ("created_at",)


@admin.register(ReadingHistory)
class ReadingHistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "viewed_at")
    search_fields = ("user__username", "book__title")
    list_filter = ("viewed_at",)
