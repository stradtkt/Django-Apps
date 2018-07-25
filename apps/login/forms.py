from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    confirm_pass = forms.CharField(max_length=30, widget=forms.PasswordInput)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    