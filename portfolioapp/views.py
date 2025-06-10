from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')

def header(request):
    return render(request, 'header.html')

def about_me(request):
    return render(request, 'about.html')

def education(request):
    return render(request, 'education.html')

# def contact(request):
#     return render(request, 'contact.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # or redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})