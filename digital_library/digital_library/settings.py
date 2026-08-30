import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#i(gm@yt6wm3kh2v8#x4ro8xh*kj8eozo1o6q93ws%o&!(1g-n"

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
    
    # 🌟 သင်ဆောက်ထားသော App များအားလုံး စနစ်တကျ ပါဝင်ပြီးဖြစ်သည်
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
        "DIRS": [BASE_DIR / 'templates'], # 🌟 HTML Templates Folder လမ်းကြောင်းမှန်အောင် ပြင်ဆင်ပြီးဖြစ်သည်
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


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# 🌟 Custom User Model Setting (ကျောင်းသားအကောင့်စနစ်အတွက်)
AUTH_USER_MODEL = 'accounts.CustomUser'


# ==============================================================================
# 📧 PASSWORD RESET & OTP EMAIL CONFIGURATION (အီးမေးလ်စနစ်)
# ==============================================================================

# 💡 အဆင့် (၁) - စမ်းသပ်ရလွယ်ကူအောင် OTP ရော Password Reset Link ရောကို 
# VS Code Terminal ထဲမှာပဲ စာသားအဖြစ် အလွယ်တကူ ထုတ်ပြပေးမည့်စနစ် (ဒါကို အဓိကသုံးပါဦးဗျာ)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# 💡 အဆင့် (၂) - အကယ်၍ တကယ့် Gmail ထဲ စာတကယ်ပို့ချင်တယ်ဆိုရင်တော့ 
# အပေါ်က အဆင့် (၁) လိုင်းကို # ခံပိတ်ပြီး၊ အောက်က ၅ ကြောင်းရဲ့ # တွေကို ဖြုတ်ပြီး ဖွင့်သုံးပါဗျာ။
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-gmail@gmail.com'       # 🔴 သင့် Gmail ရေးရန်
# EMAIL_HOST_PASSWORD = 'your-app-password'      # 🔴 Google App Password (၁၆ လုံးကုဒ်) ရေးရန်