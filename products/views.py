from django.shortcuts import redirect, resolve_url, render
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import TemplateImage
from .forms import AccountForm
from django.contrib.auth.decorators import login_required
from .template_map import template_map
from account.models import User


class TemplateListView(ListView):
    queryset = TemplateImage.objects.all()
    template_name = "temps/temps_list.html"


def show_template(request, username):
    user = User.objects.filter(username=username).first()
    if not user:
        raise Http404
    
    active_temp = user.active_template
    temp_obj = template_map[active_temp.name]['class_obj']
    
    context = {
        'object': temp_obj.objects.filter(user=user).first()
    }
    return render(request, temp_obj.template_path, context)

@login_required
def activate_template(request, temp_name):
    user = request.user
    temp = TemplateImage.objects.filter(name=temp_name).first()
    user.active_template = temp
    template_class = template_map[temp.name]['class_obj']
    temp = template_class.objects.filter(user=user).first()
    if not temp:
        template_class.objects.create(user=user)
    
    user.save()

    return redirect(resolve_url('products:template'))


@login_required
def setting_page(request):
    account_form = AccountForm(request.POST or None)
    
    temp_name = request.user.active_template.name
    template_form = template_map[temp_name]['form'](request.POST or None)
    
    context = {
        "account_form": account_form,
        "template_form": template_form
    }

    if account_form.is_valid():
        pass
    if template_form.is_valid():
        pass

    return render(request, "temps/setting.html", context)
