# 📂 borrow/admin.py ထဲတွင် အခုလို ပြင်ရေးနိုင်သည်
from django.contrib import admin
from .models import BorrowRecord

class BorrowBookAdmin(admin.ModelAdmin):
    # 🌟 Admin Panel Table ပေါ်တွင် အတန်းလိုက် ပြပေးမည့် Column မျာ:
    list_display = ('user', 'book', 'borrow_date', 'due_date', 'return_date')
    
    # 🌟 Status အလိုက် (ဥပမာ- ငှားဆဲ၊ အပ်ပြီး) ဘေးကနေ Filter စစ်ထုတ်ကြည့်နိုင်ရန်
    list_filter = ('borrow_date', 'due_date')
    
    # 🌟 ကျောင်းသားနာမည် သို့မဟုတ် စာအုပ်နာမည်ဖြင့် ရှာဖွေနိုင်ရန်
    search_fields = ('user__username', 'book__title')

# Model နှင့် Custom Admin Class ကို တွဲပြီး Register လုပ်ခြင်း
admin.site.register(BorrowRecord, BorrowBookAdmin)