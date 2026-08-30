import random
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
from .forms import StudentSignupForm # 🌟 Forms.py မှလှမ်းခေါ်ခြင်း
from borrow.models import BorrowRecord
from books.models import Bookmark, ReadingHistory
from django.views.decorators.csrf import csrf_exempt

# 1. Signup Logic
def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_verified = False
            user.set_password(form.cleaned_data['password'])
            user.role = 'student'
            
            # 6-Digit OTP Code ထုတ်ခြင်း
            otp = str(random.randint(100000, 999999))
            user.otp_code = otp
            user.save()
            
            print("\n" + "="*50)
            print(f"🌟🌟🌟🌟 [NEW STUDENT OTP CODE]: {otp} 🌟🌟🌟🌟")
            print("="*50 + "\n")
            
            # Email ပို့ရန် ကြိုးစားခြင်း
            try:
                send_mail(
                    'Smart Library - Email Verification Code',
                    f'မင်္ဂလာပါ {user.username}၊ လူကြီးမင်း၏ OTP သီးသန့်ကုဒ်မှာ {otp} ဖြစ်ပါသည်။',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
            except Exception:
                print(f"\n🌟🌟🌟🌟 [DEVELOPER OTP CODE]: {otp} 🌟🌟🌟🌟\n")

            request.session['otp_username'] = user.username
            return redirect('verify_otp')
    else:
        form = StudentSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

# 2. OTP Verification Logic
def verify_otp(request):
    username = request.session.get('otp_username')
    if not username:
        return redirect('signup')
        
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        try:
            user = CustomUser.objects.get(username=username)
            if user.otp_code == user_otp:
                user.is_verified = True
                user.otp_code = None
                user.save()
                login(request, user)
                messages.success(request, "အီးမေးလ်အတည်ပြုခြင်း အောင်မြင်ပါသည်။")
                return redirect('profile')
            else:
                messages.error(request, "OTP ကုဒ်မှားယွင်းနေပါသည်။")
        except CustomUser.DoesNotExist:
            return redirect('signup')
            
    return render(request, 'accounts/verify_otp.html')

# 3. Login Logic (Fixed Namespace & Redirect Loop)
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_exists = CustomUser.objects.filter(username=username).exists()
        
        if not user_exists:
            messages.error(request, "ဤအသုံးပြုမည့်အမည် (Username) ဖြင့် အကောင့်မရှိသေးပါ။ ကျေးဇူးပြု၍ အကောင့်အရင်ဆောက်ပေးပါဗျာ။")
        else:
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # Admin သို့မဟုတ် Staff ဖြစ်ပါက Path တိုက်ရိုက်သုံးရန် (Loop မပတ်စေရန်)
                if user.is_superuser or user.is_staff:
                    login(request, user)
                    return redirect('/dashboard/') 

                if user.role == 'student' and not user.is_verified:
                    request.session['otp_username'] = user.username
                    return redirect('verify_otp')
                    
                login(request, user)
                return redirect('profile' if user.role == 'student' else '/dashboard/')
            else:
                messages.error(request, "ရိုက်ထည့်လိုက်သော စကားဝှက် (Password) မှားယွင်းနေပါသည်။ ပြန်လည်စစ်ဆေးပေးပါ။")
    else:
        form = AuthenticationForm()
        
    return render(request, 'accounts/login.html', {'form': form})

# 4. Logout Logic
def user_logout(request):
    logout(request)
    return redirect('login')

# 5. Student Profile View
def student_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    my_borrows = BorrowRecord.objects.filter(user=request.user, return_date__isnull=True)
    total_fine = sum(record.calculate_fine for record in my_borrows)
    saved_books = Bookmark.objects.filter(user=request.user).select_related('book')[:6]
    recent_books = ReadingHistory.objects.filter(user=request.user).select_related('book')[:6]
    
    context = {
        'my_borrows': my_borrows,
        'total_fine': total_fine,
        'borrowed_count': my_borrows.count(),
        'saved_books': saved_books,
        'recent_books': recent_books,
    }
    return render(request, 'accounts/profile.html', context)

# 6. Home View (Fixed Loop Issue)
def home(request):
    # အကယ်၍ အကောင့်ဝင်ပြီးသားဆိုလျှင် လိုရာခရီးသို့ တိုက်ရိုက်ပို့မည် (Loop မပတ်စေရန် စစ်ဆေးပြီး)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        return redirect('/dashboard/')

    return render(request, 'home.html')

# =========================================================================
# 🌟 SMART PASSWORD RESET WITH 6-DIGIT OTP (CUSTOM FLOW)
# =========================================================================

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email).first()
        
        if user:
            otp = str(random.randint(100000, 999999))
            user.otp_code = otp
            user.save()
            
            request.session['reset_email'] = email
            print("\n" + "="*50)
            print(f"🌟🌟🌟🌟 [PASSWORD RESET OTP CODE]: {otp} 🌟🌟🌟🌟")
            print("="*50 + "\n")

            try:
                send_mail(
                    'Smart Library - Password Reset Code',
                    f'မင်္ဂလာပါ {user.username}၊ လူကြီးမင်း၏ စကားဝှက်ပြောင်းလဲရန် OTP ကုဒ်မှာ {otp} ဖြစ်ပါသည်။',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
            except Exception:
                print(f"\n🌟🌟🌟🌟 [PASSWORD RESET OTP CODE]: {otp} 🌟🌟🌟🌟")
                
            return redirect('password_reset_done')
        else:
            messages.error(request, "ဤအီးမေးလ်ဖြင့် အကောင့်ဖွင့်ထားခြင်း မရှိသေးပါဗျာ။")
            
    return render(request, 'accounts/password_reset.html')

def password_reset_done_view(request):
    return render(request, 'accounts/password_reset_done.html')

def password_reset_confirm_otp(request):
    email = request.session.get('reset_email')
    if not email:
        return redirect('password_reset')
        
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        try:
            user = CustomUser.objects.get(email=email)
            if user.otp_code == user_otp:
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.otp_code = None 
                    user.save()
                    messages.success(request, "စကားဝှက်အသစ် ပြောင်းလဲခြင်း အောင်မြင်ပါသည်။")
                    return redirect('login')
                else:
                    messages.error(request, "စကားဝှက်နှစ်ခု ကိုက်ညီမှု မရှိပါ။")
            else:
                messages.error(request, "OTP ကုဒ် ၆ လုံး မှားယွင်းနေပါသည်။")
        except CustomUser.DoesNotExist:
            return redirect('password_reset')
            
    return render(request, 'accounts/password_reset_confirm_otp.html')