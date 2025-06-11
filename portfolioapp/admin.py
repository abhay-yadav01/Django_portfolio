from django.contrib import admin
from .models import Contact
from .models import Feedback

admin.site.register(Contact)
admin.site.register(Feedback)