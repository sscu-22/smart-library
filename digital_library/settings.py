'''
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2ho2nbj8(rutseedgaalm41n60q=p^avtke(zsmvg*l5(e_lr#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 🌟 သင်ဆောက်ထားသော App များ
    'accounts',
    'books',
    'borrow',
    'dashboard',
    'search',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "digital_library.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "digital_library.wsgi.application"

# Database (SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# 🌟 Custom User Model Setting (ဒီနေရာတွင် ထားပေးပါ)
AUTH_USER_MODEL = 'accounts.CustomUser'

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / 'static']  # အရှေ့က # ကို ဖြုတ်ပြီး အသက်သွင်းလိုက်ပါပြီ
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# 📂 settings.py ၏ အောက်ခြေတွင် ထည့်ရန်
#LOGOUT_REDIRECT_URL = '/'  # 🌟 Logout ဖြစ်ပြီးလျှင် http://127.0.0.1:8000/ သို့ တိုက်ရိုက်ပို့ခိုင်းခြင်း
# 🌟 ၁။ Logout ဖြစ်ပြီးလျှင် Login စာမျက်နှာသို့ တိုက်ရိုက် ပို့ခိုင်းခြင်း
LOGOUT_REDIRECT_URL = '/login/'  

# 🌟 ၂။ အကောင့်ဝင်ပြီးလျှင် Dashboard သို့ ပို့ပေးရန် ညွှန်ကြားခြင်း
LOGIN_REDIRECT_URL = '/dashboard/'  

# 🌟 ၃။ အကောင့်မဝင်ရသေးလျှင် သို့မဟုတ် Error တက်လျှင် မူရင်း /accounts/login/ သို့မသွားဘဲ
# မိတ်ဆွေဆောက်ထားသည့် /login/ စာမျက်နှာသို့သာ အတင်းသွားခိုင်းရန် (ဤလိုင်းက အဓိက တရားခံကို ရှင်းပါလိမ့်မည်)
LOGIN_URL = '/login/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
'''
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2ho2nbj8(rutseedgaalm41n60q=p^avtke(zsmvg*l5(e_lr#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['smartlibrary.ucsm.edu.mm']
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    # 🌟 UI ကို Left Sidebar နှင့် ပြောင်းလဲရန် (Logout/Add/Change အကုန်အလုပ်လုပ်စေမည့်အပြင်အဆင်)
    #"jazzmin", 
    
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # 🌟 သင်ဆောက်ထားသော App များ
    'accounts',
    'books',
    'borrow',
    'dashboard',
    'search',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "digital_library.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "digital_library.wsgi.application"

# Database (SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# 🌟 Custom User Model Setting
AUTH_USER_MODEL = 'accounts.CustomUser'

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / 'static']
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 🌟 Redirect URLs Settings (မပြောင်းလဲဘဲ မူရင်းအတိုင်း ထားရှိပါသည်)
LOGOUT_REDIRECT_URL = '/login/'  
LOGIN_REDIRECT_URL = '/dashboard/'  
LOGIN_URL = '/login/'

# ==============================================================================
# 🌟 JAZZMIN ERROR-FREE PERFECT SETTINGS
# ==============================================================================

JAZZMIN_SETTINGS = {
    "site_title": "UCSM Smart Digital Library",
    "site_header": "UCSM Smart Digital Library",
    "site_brand": "UCSM Admin Core",
    "welcome_sign": "Welcome to UCSM Digital Library Admin Portal",
    "copyright": "UCSM Smart Digital Library & Management Portal",
    
    # 📌 Left Sidebar Navigation ကို စနစ်တကျ ဖွင့်ထားခြင်း
    "navigation_expanded": True,
    "show_sidebar": True,
    
    # ⚠️ Logout ပြဿနာကို ဖြေရှင်းရန် - မူရင်း Django Admin Logout URL ကို အသုံးပြုခိုင်းခြင်း
    "use_dot_urls": False,
    
    # 📌 သင့် App တစ်ခုချင်းစီအတွက် ဘယ်ဘက် Sidebar တွင် ပြသမည့် Icons ကလေးများ
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.Group": "fas fa-users",
        "accounts.CustomUser": "fas fa-user-graduate",
        "books.Book": "fas fa-book",
        "borrow.Borrow": "fas fa-hand-holding", 
        "dashboard.Dashboard": "fas fa-tachometer-alt",
        "search.Search": "fas fa-search",
    },
    
    "use_google_fonts": True,
}

# 🎨 လက်ရှိ image_f94a0c.jpg နှင့် အနီးစပ်ဆုံး Dark UI ဖြစ်အောင် ချိန်ညှိခြင်း
JAZZMIN_UI_TWEAKS = {
    "theme": "darkly", 
    "sidebar_theme": "sidebar-dark-indigo", 
    "sidebar": "nav-sidebar nav-flat nav-child-indent",
    "navbar": "navbar-dark navbar-indigo",
}