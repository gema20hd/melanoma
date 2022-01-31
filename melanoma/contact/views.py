from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.


#@method_decorator(login_required, name='dispatch')
@login_required
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            subject = request.POST.get('subject', '')
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamor
            email = EmailMessage(
                subject,
                "\n{}".format(content),  to=[email])
            try:
                email.send()
                return redirect(reverse(contact)+"?OK")
            except:
                return redirect(reverse(contact)+"?FAIL")

    return render(request, "contact/contact.html", {'form': contact_form})
