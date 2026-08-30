from django.contrib import admin
from django.urls import path, include
from search import views as search_views
from books import views as book_views
from accounts import views as accounts_views  
from django.contrib.auth import views as auth_views

# 📂 digital_library/urls.py ထဲတွင် သွားရောက်ပြင်ဆင်ရန်

urlpatterns = [
    path('', accounts_views.home, name='home'),
    path('admin/', admin.site.urls),
    
    # User Pages (Login, Signup, Profile) အတွက် လင့်ခ်များ
    path('signup/', accounts_views.student_signup, name='signup'),
    path('login/', accounts_views.user_login, name='login'),
    path('logout/', accounts_views.user_logout, name='logout'),
    path('profile/', accounts_views.student_profile, name='profile'),
    
    # OTP စစ်ဆေးခြင်းနှင့် စာအုပ်ငှားခြင်း လမ်းကြောင်းများ
    path('verify-otp/', accounts_views.verify_otp, name='verify_otp'),
    path('borrow-book/<int:book_id>/', search_views.quick_borrow, name='quick_borrow'), 
    
    # SMART PASSWORD RESET WITH 6-DIGIT OTP
    path('password-reset/', accounts_views.password_reset_request, name='password_reset'),
    path('password-reset/done/', accounts_views.password_reset_done_view, name='password_reset_done'),
    path('password-reset-confirm-otp/', accounts_views.password_reset_confirm_otp, name='password_reset_confirm'),

    # -------------------------------------------------------------------------
    # 🌟 [ဒီလိုင်းအသစ်ကို တိုးပေးလိုက်ပါ] 
    # Browser က /accounts/login/ ဟု ခေါ်လျှင်လည်း Django default စနစ်ဆီ မသွားစေဘဲ
    # မိတ်ဆွေ ရေးထားပြီးသား Custom 'user_login' ဆီသို့ အတင်း လွှဲပေးလိုက်ခြင်း ဖြစ်ပါသည်
    # -------------------------------------------------------------------------
    path('accounts/login/', accounts_views.user_login, name='accounts_login'),

    # accounts/logout/ ကြားဖြတ်ဖမ်းခြင်း (ပြီးခဲ့သည့်အဆင့်တွင် အောင်မြင်ခဲ့သောလိုင်း)
    path('accounts/logout/', accounts_views.user_logout, name='accounts_logout'),

    # Django built-in auth စနစ်
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('dashboard/', include('dashboard.urls',namespace='dashboard')),
    path('search/', search_views.search_books, name='search'),
    path('search/autocomplete/', search_views.autocomplete_books, name='autocomplete_books'),
    path('books/<int:book_id>/', book_views.book_detail, name='book_detail'),
    path('books/<int:book_id>/bookmark/', search_views.toggle_bookmark, name='toggle_bookmark'),
]
