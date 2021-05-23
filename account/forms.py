from django import forms
from .models import User


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your full name"}))

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "enter your email"}))

    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "enter your message"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if "gmail.com" not in email:
            raise forms.ValidationError("Email has to be gmail.com")

        return email


class LoginForm(forms.Form):
    userName = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your user name"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your password"})
    )


class RegisterForm(forms.Form):
    error_css_class = 'text-danger'
    required_css_class = 'required'
    userName = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your user name"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "enter your email"}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your password"})
    )

    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your password"})
    )

    def clean_userName(self):
        userName = self.cleaned_data.get('userName')
        qs = User.objects.filter(username=userName)
        if qs.exists():
            raise forms.ValidationError("نام کاربری موجود است")
        return userName

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("ایمیل موجود است")
        return email

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("پسورد ها باید برابر باشند")
        return password2
