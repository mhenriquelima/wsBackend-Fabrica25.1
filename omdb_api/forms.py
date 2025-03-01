from django import forms

class movieForm(forms.Form):
    title = forms.CharField(label='Search', max_length=100)

class loginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    