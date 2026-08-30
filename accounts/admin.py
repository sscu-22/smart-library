from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Admin Panel တွင် မြင်တွေ့ရမည့် Column များ
    list_display = ['username', 'email', 'role', 'student_id', 'is_staff']
    
    # Admin Panel တွင် Edit လုပ်ရမည့် Form ထဲ၌ Role နှင့် Student ID ကို ထည့်သွင်းခြင်း
    fieldsets = UserAdmin.fieldsets + (
        ('Smart Library Role Settings', {'fields': ('role', 'student_id', 'max_borrow_limit')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)