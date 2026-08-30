from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Super Admin'),
        ('librarian', 'Librarian/Staff'),
        ('student', 'Student Member'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    student_id = models.CharField(max_length=20, blank=True, null=True, unique=True) # Unique ဖြစ်ရပါမည်
    max_borrow_limit = models.IntegerField(default=5)
    
    # 🌟 OTP System Fields
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False) # OTP အောင်မြင်မှ True ဖြစ်မည်

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"