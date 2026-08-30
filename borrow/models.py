from django.db import models
from django.conf import settings
from books.models import Book
from django.utils import timezone

# 🌟 ဒီ Model နာမည် 'BorrowRecord' စာလုံးပေါင်း တိကျမှန်ကန်ရပါမယ်
class BorrowRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    
    @property
    def calculate_fine(self):
        if not self.return_date and timezone.now().date() > self.due_date:
            return (timezone.now().date() - self.due_date).days * 500
        return 0

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"