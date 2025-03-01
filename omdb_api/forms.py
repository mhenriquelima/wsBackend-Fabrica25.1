from django import forms

class movieForm(forms.Form):
    title = forms.CharField(label='Search', max_length=100)
    