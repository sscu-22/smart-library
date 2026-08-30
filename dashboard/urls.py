# dashboard/urls.py (မိတ်ဆွေအခုဆောက်လိုက်သော ဖိုင်အသစ်ထဲတွင် ထည့်ရန်)

from django.urls import path
from . import views
app_name = 'dashboard'
urlpatterns = [
    # http://127.0.0.1:8000/dashboard/ လို့ ရိုက်ရင် views.py ထဲက dashboard function ကို သွားခေါ်မည့်လမ်းကြောင်း
    path('', views.admin_dashboard, name='dashboard_home'), 
]