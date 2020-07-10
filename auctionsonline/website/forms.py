from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=45)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=45)
    password2 = forms.CharField(max_length=45)
	
class LoginForm(forms.Form):
    username = forms.CharField(max_length=45)
    password = forms.CharField(max_length=45)