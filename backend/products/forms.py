from django import forms
#forms alanı göstermelik seriazlırda işler

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = [
            'title',
            'content',
            'price'
        ]