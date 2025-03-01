from django import forms
from .models import reviewModel

class movieForm(forms.Form):
    title = forms.CharField(label='Search', max_length=100)

class reviewForm(forms.ModelForm):
    class Meta:
        model = reviewModel
        fields = ['review_text', 'rating']
    