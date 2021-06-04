from django.shortcuts import redirect, resolve_url, render
from django.http import Http404
from django.views.generic import ListView
from .models import TemplateImage
from .forms import AccountForm
from django.contrib.auth.decorators import login_required
from .template_map import template_map
from account.models import User
from django.contrib.auth import logout

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
    account_form = AccountForm(
        request.POST or None, request.FILES or None, instance=request.user)

    active_template = request.user.active_template
    template_form = template_map[active_template.name]['form']
    template_obj = template_map[active_template.name]['class_obj'].objects.get(
        user=request.user)

    template_form = template_form(
        request.POST or None, request.FILES or None,
        instance=template_obj)

    context = {
        "account_form": account_form,
        "template_form": template_form,
        "temp_name": active_template.name,
    }

    if account_form.is_valid():
        account_form.save()
    if template_form.is_valid():
        template_obj = template_form.save()
        template_obj.user = request.user
        template_obj.save()

    return render(request, "setting/setting.html", context)

