# 📂 dashboard/views.py

from django.db.models import Count
from django.shortcuts import render, redirect
from borrow.models import BorrowRecord
from books.models import Book, Bookmark, Category
from accounts.models import CustomUser

def admin_dashboard(request):
    # 🌟 Security Check Flow:
    # ၁။ Login မဝင်ရသေးရင် မိတ်ဆွေရဲ့ ပင်မစာမျက်နှာ 'home' (accounts_views.home) ဆီကို တိုက်ရိုက် မောင်းထုတ်မည်။
    if not request.user.is_authenticated:
        return redirect('home')  
        
    # ၂။ Login ဝင်ထားသော်လည်း Role က ကျောင်းသား (Student) ဖြစ်နေပါကလည်း 'home' (ပင်မစာမျက်နှာ) ဆီသို့ပဲ ပြန်လွှတ်မည်။
    if request.user.role == 'student':
        return redirect('home')  
        
    # -------------------------------------------------------------------------
    # အကယ်၍ Admin သို့မဟုတ် Staff ဖြစ်ပါက အောက်ပါအတိုင်း ဒိုင်ယာဂရမ်/ဒေတာများ ဆက်လုပ်မည်
    total_books = Book.objects.count()
    total_users = CustomUser.objects.count()
    active_borrows = BorrowRecord.objects.filter(return_date__isnull=True).count()
    
    popular_books = Book.objects.order_by('-views_count')[:5]
    book_labels = [book.title for book in popular_books]
    book_views = [book.views_count for book in popular_books]
    saved_count = Bookmark.objects.count()
    low_stock_books = Book.objects.filter(available_copies__lte=1).order_by('available_copies', 'title')[:5]
    category_stats = Category.objects.annotate(total=Count('books')).order_by('-total')[:5]

    context = {
        'total_books': total_books, 
        'total_users': total_users, 
        'active_borrows': active_borrows,
        'saved_count': saved_count,
        'low_stock_books': low_stock_books,
        'category_stats': category_stats,
        'book_labels': book_labels, 
        'book_views': book_views,
    }
    return render(request, 'dashboard/index.html', context)
