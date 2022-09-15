from django import forms
from matplotlib import widgets
from .models import Book

class RentBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['status']

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }