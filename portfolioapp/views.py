from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Feedback

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

def feedback_form(request):
    return render(request, 'feedback.html')

def submit_feedback(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        try:
            rating = int(rating)
        except (TypeError, ValueError):
            rating = 0

        Feedback.objects.create(
            name=request.POST['name'],
            email=request.POST.get('email', ''),
            message=request.POST['message'],
            rating=rating
        )
        return render(request, 'thankyou.html')
    return redirect('feedback')
