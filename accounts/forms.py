# accounts/forms.py ဟူသော ဖိုင်အသစ်ထဲတွင် ထည့်ရန်ကုဒ်
from django import forms
from django.forms import ModelForm
from .models import CustomUser

class StudentSignupForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-slate-900 border border-slate-800 rounded-xl px-4 py-3 text-slate-200 w-full focus:outline-none focus:border-indigo-500'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-slate-900 border border-slate-800 rounded-xl px-4 py-3 text-slate-200 w-full focus:outline-none focus:border-indigo-500'
    }))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'student_id']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'bg-slate-900 border border-slate-800 rounded-xl px-4 py-3 text-slate-200 w-full focus:outline-none focus:border-indigo-500'}),
            'email': forms.EmailInput(attrs={'class': 'bg-slate-900 border border-slate-800 rounded-xl px-4 py-3 text-slate-200 w-full focus:outline-none focus:border-indigo-500'}),
            'student_id': forms.TextInput(attrs={'class': 'bg-slate-900 border border-slate-800 rounded-xl px-4 py-3 text-slate-200 w-full focus:outline-none focus:border-indigo-500'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("စကားဝှက်နှစ်ခု ကိုက်ညီမှု မရှိပါ။")
        return cleaned_data