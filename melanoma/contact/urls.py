from django.contrib import admin
from django.urls import path
from . import views
#from contact.views import Contact

urlpatterns = [

    # paths de core

    path('contact/', views.contact, name="contact"),
    #path('contact/', Contact.as_view(), name='contact'),

]
