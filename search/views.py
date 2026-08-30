import datetime

from django.contrib import messages
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from books.models import Book, Bookmark, Category, ReadingHistory
from borrow.models import BorrowRecord


def search_books(request):
    query = request.GET.get("q", "").strip()
    category_id = request.GET.get("category", "").strip()
    language = request.GET.get("language", "").strip()
    tag = request.GET.get("tag", "").strip()
    sort = request.GET.get("sort", "latest").strip()

    books = Book.objects.select_related("category").all()

    if query:
        books = books.filter(
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(category__name__icontains=query)
            | Q(code_number__icontains=query)
            | Q(tags__icontains=query)
            | Q(language__icontains=query)
        )

    if category_id:
        books = books.filter(category_id=category_id)

    if language:
        books = books.filter(language__iexact=language)

    if tag:
        books = books.filter(tags__icontains=tag)

    sort_options = {
        "popular": "-views_count",
        "title": "title",
        "latest": "-created_at",
    }
    books = books.order_by(sort_options.get(sort, "-created_at"), "title")

    saved_book_ids = set()
    recent_books = []
    recommended_books = Book.objects.none()

    if request.user.is_authenticated:
        saved_book_ids = set(
            Bookmark.objects.filter(user=request.user).values_list("book_id", flat=True)
        )
        recent_books = (
            Book.objects.filter(reading_history__user=request.user)
            .select_related("category")
            .order_by("-reading_history__viewed_at")[:5]
        )
        recent_categories = [
            item.category_id for item in recent_books if item.category_id is not None
        ]
        if recent_categories:
            recommended_books = (
                Book.objects.filter(category_id__in=recent_categories)
                .exclude(id__in=[item.id for item in recent_books])
                .annotate(save_count=Count("bookmarks"))
                .order_by("-save_count", "-views_count")[:6]
            )

    categories = Category.objects.all()
    languages = (
        Book.objects.exclude(language="")
        .values_list("language", flat=True)
        .distinct()
        .order_by("language")
    )
    tags = sorted({tag for book in Book.objects.exclude(tags="") for tag in book.tag_list})

    context = {
        "results": books,
        "query": query,
        "categories": categories,
        "languages": languages,
        "tags": tags,
        "selected_category": category_id,
        "selected_language": language,
        "selected_tag": tag,
        "selected_sort": sort,
        "saved_book_ids": saved_book_ids,
        "recent_books": recent_books,
        "recommended_books": recommended_books,
    }
    return render(request, "search/search.html", context)


def autocomplete_books(request):
    query = request.GET.get("q", "").strip()
    suggestions = []

    if query:
        suggestions = list(
            Book.objects.filter(
                Q(title__icontains=query)
                | Q(author__icontains=query)
                | Q(code_number__icontains=query)
                | Q(tags__icontains=query)
            )
            .order_by("title")
            .values("id", "title", "author", "code_number")[:8]
        )

    return JsonResponse({"results": suggestions})


def toggle_bookmark(request, book_id):
    if not request.user.is_authenticated:
        return redirect("login")

    book = get_object_or_404(Book, id=book_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, book=book)
    if not created:
        bookmark.delete()

    next_url = request.POST.get("next") or request.GET.get("next") or "search"
    return redirect(next_url)


def quick_borrow(request, book_id):
    if not request.user.is_authenticated:
        return redirect("login")

    book = get_object_or_404(Book, id=book_id)

    if book.available_copies <= 0:
        messages.error(request, "This book is not available right now.")
        return redirect("search")

    already_borrowed = BorrowRecord.objects.filter(
        user=request.user,
        book=book,
        return_date__isnull=True,
    ).exists()
    if already_borrowed:
        messages.info(request, "You already borrowed this book.")
        return redirect("profile")

    BorrowRecord.objects.create(
        user=request.user,
        book=book,
        due_date=datetime.date.today() + datetime.timedelta(days=14),
    )

    book.available_copies -= 1
    book.save(update_fields=["available_copies"])

    messages.success(request, f"You borrowed '{book.title}' successfully.")
    return redirect("profile")
