from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/email/', EmailUpdate.as_view(), name='profile_email'),

]
