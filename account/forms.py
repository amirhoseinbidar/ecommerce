from django import forms
from .models import User
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core import validators
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
User = get_user_model()
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

class EmailService:
    @staticmethod
    def send_email(subject,to,template_name,context):
        html_message=render_to_string(template_name,context)
        plain_message=''
        send_mail(subject,plain_message,'myzshop1400@gmail.com',to,html_message=html_message)

class EmailSend(forms.Form):
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'لطفا ایمیل خود را وارد نمایید'}),
        label='ایمیل',
        validators=[
            validators.EmailValidator(message='ایمیل وارد شده معتبر نمی باشد')
        ]
    )
class PasswordChange(forms.Form):
    userName = forms.CharField(
         label="نام کاربری",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام کاربری خود را وارد نمایید"})
    )

    password = forms.CharField(
         label="رمز عبور جدید",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "رمز عبور خود را وارد نمایید"})
    )

    password2 = forms.CharField(
        label="تایید رمز عبور جدید",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "رمز عبور خود را وارد نمایید"})
    )
    def clean_userName(self):
        userName = self.cleaned_data.get('userName')
        qs = User.objects.filter(username=userName)
        if not qs.exists():
            raise forms.ValidationError("نام کاربری موجود نیست")
        return userName
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("پسورد ها باید برابر باشند")
        return password2