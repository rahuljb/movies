from django import forms
from .models import movies


class movieForm(forms.ModelForm):
    class Meta:
        model = movies
        fields = ['img', 'name', 'desc', 'year']
