"""
URL configuration for digital_library project.
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    # 🌟 အရေးကြီးဆုံးအချက်: ပင်မ Root Path "" ကို အပေါ်ဆုံး (ထိပ်ဆုံး) မှာ ထားရပါမယ်။
    path("", RedirectView.as_view(url="/login/", permanent=False), name="home"),
    
    # Admin path ကို အောက်သို့ ရွှေ့ပေးရပါမယ်။
    path("admin/", admin.site.urls),
]