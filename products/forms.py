from django import forms
from account.models import User
from .models import TemplateTypeOne, TemplateTypeTwo


class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'avatar']


class TemplateTypeOneForm(forms.ModelForm):
    class Meta:
        model = TemplateTypeOne
        fields = '__all__'


class TemplateTypeTwoForm(forms.ModelForm):
    class Meta:
        model = TemplateTypeTwo
        fields = '__all__'
