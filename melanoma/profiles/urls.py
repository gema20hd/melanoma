from django.urls import path
from .views import ProfileListView, ProfileDetailView

#urls de la aplicacion profiles
profiles_patterns = ([
    path('', ProfileListView.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
], "profiles")
