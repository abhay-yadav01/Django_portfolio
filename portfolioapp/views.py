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
            contact = form.save()

            # Send Thank You Email
            send_mail(
                'Thanks for reaching out!',
                f"Hi {contact.first_name},\n\nThanks for contacting me. I’ll get back to you soon!\n\n– Abhay",
                settings.EMAIL_HOST_USER,
                [contact.email],
                fail_silently=False,
            )

            return redirect('thank_you')  # You can create a thank you page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})