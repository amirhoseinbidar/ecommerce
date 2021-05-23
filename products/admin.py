from django.contrib import admin
from .models import (TemplateTypeOne, TemplateTypeTwo, TemplateImage)

admin.site.register((TemplateTypeOne, TemplateTypeTwo, TemplateImage))