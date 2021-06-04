from django.contrib.auth import logout
from django.urls import path
from . import views

app_name = 'products' 
urlpatterns = [
    path('', views.TemplateListView.as_view(), name='template'),
    path('setting/', views.setting_page, name='setting'),
    path('show/<str:username>/', views.show_template, name='show'),
    path('activate_tempalte/<str:temp_name>/', views.activate_template, name='activate_tempalte'),

]
