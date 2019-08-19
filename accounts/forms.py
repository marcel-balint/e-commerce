from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class GuestForm(forms.Form):
    email = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email"
            }
        )
    )
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput)

    def clean(self):
        # Check if passords match
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Passords must match.")
        return data

    def clean_username(self):
        # Check is there are duplicate usernmaes
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken.")
        return username

    def clean_email(self):
        # Check is there are duplicate email addresses
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError("Email addresses must be unique.")
        return email
