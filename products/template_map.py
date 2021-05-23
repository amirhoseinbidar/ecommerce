from .models import TemplateTypeOne, TemplateTypeTwo
from .forms import TemplateTypeOneForm, TemplateTypeTwoForm

template_map = {
    'type_one': {
        'class_obj': TemplateTypeOne,
        'form': TemplateTypeOneForm,
    },
    'type_two': {
        'class_obj': TemplateTypeTwo,
        'form': TemplateTypeTwoForm,
    }
}