"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from account.views import home_page, about_page, contact_page, login_page, register_page
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('about-us', about_page),
    path('contact-us', contact_page),
    path('register', register_page, name='register'),
    path('templates/', include("products.urls")),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='resetting/password_rest.html'),
         name='password_reset'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='resetting/password_rest_sent.html'),
         name='password_reset_done'),

    path('reset<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='resetting/password_rest_form.html'),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='resetting/password_reset_done'),
         name='reset_password_complete'),
]
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
