from dataclasses import field
from allauth.account.forms import SignupForm,LoginForm
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    bio = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control','rows':3,'cols':5}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        self.fields['password1'].help_text = ''
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control'})

class CustomLoginForm(LoginForm): 
    
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        self.fields['login'].widget = forms.EmailInput(attrs={'class':'form-control'})

    