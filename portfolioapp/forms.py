from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'service', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Firstname'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Lastname'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'service': forms.Select(choices=[
                ('', 'Select a service'),
                ('web', 'Web Development'),
                ('design', 'UI/UX Design'),
            ]),
            'message': forms.Textarea(attrs={'placeholder': 'Type your message here.', 'rows': 5}),
        }