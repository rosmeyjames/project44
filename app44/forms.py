from django import forms
from .models import *

from.models import book,author
class authorform(forms.ModelForm):
    class Meta:
        model=author
        fields='__all__'
class bookform(forms.ModelForm):
    class Meta:
        model=book
        fields='__all__'