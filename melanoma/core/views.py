from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required

# Create your views here.
# renderizamos el url los templates indicados


class Inicio(LoginRequiredMixin, generic.TemplateView):
    template_name = 'core/home.html'
    login_url = 'login'


@login_required
def home(request):
    return render(request, "core/home.html")
