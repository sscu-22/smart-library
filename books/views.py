from django.db.models import Count
from django.shortcuts import get_object_or_404, render

from .models import Book, Bookmark, ReadingHistory


def book_detail(request, book_id):
    book = get_object_or_404(Book.objects.select_related("category"), id=book_id)
    book.views_count += 1
    book.save(update_fields=["views_count"])

    is_saved = False
    if request.user.is_authenticated:
        ReadingHistory.objects.update_or_create(user=request.user, book=book)
        is_saved = Bookmark.objects.filter(user=request.user, book=book).exists()

    related_books = (
        Book.objects.filter(category=book.category)
        .exclude(id=book.id)
        .annotate(save_count=Count("bookmarks"))
        .order_by("-save_count", "-views_count")[:4]
        if book.category_id
        else Book.objects.none()
    )

    return render(
        request,
        "books/book_detail.html",
        {
            "book": book,
            "is_saved": is_saved,
            "related_books": related_books,
        },
    )
