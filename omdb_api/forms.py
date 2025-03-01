from django import forms
from .models import Review

class movieForm(forms.Form):
    title = forms.CharField(label='Search', max_length=100)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']
    