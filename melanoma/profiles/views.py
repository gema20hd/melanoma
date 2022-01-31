from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile


# Create your views here.
#listar todos usuarios
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 10

#detalle de todos los usuarios
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    
#obtener los username del usuario
    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
    
