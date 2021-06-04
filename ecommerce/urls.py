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
from account.views import home_page, about_page, contact_page, login_page, register_page,logout_page,forget_password,send_email_done,change_password
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('about-us', about_page),
    path('contact-us', contact_page),
    path('register', register_page, name='register'),
    path('logout', logout_page, name='logout'),
    path('templates/', include("products.urls")),
    path('forget-password/',forget_password),
    path('forget-password/send-email-sucessfull/',send_email_done,name='send-email-sucessfull'),
    path('change-password/',change_password,name='change_password'),
    
]
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
