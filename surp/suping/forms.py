
from django import forms
from django.contrib.auth.models import User

class registerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email','password', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].help_text = ''

class loginForm(forms.Form):
    email = forms.EmailField(max_length=100, label='email')
    password = forms.CharField(widget=forms.PasswordInput, label='password')
