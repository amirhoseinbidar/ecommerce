from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm,EmailSend,EmailService,PasswordChange
from django.contrib.auth import login , get_user_model,authenticate, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib import messages

User = get_user_model()
UserModel = get_user_model()



def home_page(request):
    print(f"is user logged in : {request.user.is_authenticated}")
    context = {
        "title": "صفحه ی اصلی",

    }

    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "درباره ما",
        "content": "درمورد ما بخوانید"
    }

    return render(request, "about_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "تماس با ما",
        "content": "this is contact page",
        "form": contact_form
    }
    contactinfolist = []
    if contact_form.is_valid():
        result = contact_form.cleaned_data
        contactinfolist.append(result)
        print(contactinfolist)

    return render(request, 'contact/view.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect(reverse('products:template'))

    context = {
        "form": form
    }
    if form.is_valid():
        userName = form.cleaned_data.get("userName")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            context["form"] = LoginForm()
            return redirect(reverse('products:template'))
        else:
            context['error'] = 'کاربری با این مشخصات موجود نیست'

    return render(request, "auth/login.html", context)





def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        userName = form.cleaned_data.get("userName")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        User.objects.create_user(
            username=userName, email=email, password=password)
        return redirect(reverse('products:template'))

    return render(request, "auth/register.html", context)

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")


def forget_password(request):
    email_form=EmailSend(request.POST or None)
    if email_form.is_valid():
        email=email_form.cleaned_data.get('email')
        EmailService.send_email('ایمیل فراموشی رمز عبور',[email],'emails/test_email.html',
        {
            'title':'سلام',

        })
    context={
        'email_form':email_form
    }
    return render(request, 'auth/forget-password.html', context)

def send_email_done(request):
    context={
        'text':'ایمیل حاوی تغیر رمز عبور برای شما ارسال گردید'
    }
    return render(request , 'auth/send-email-done.html' , context)


def change_password(request):

    form = PasswordChange(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        userName = form.cleaned_data.get("userName")
        password = form.cleaned_data.get("password")
        user=User.objects.filter(username=userName).first()
    
        user.set_password(password) 
        user.save()
        

    return render(request, "auth/change-password.html", context)