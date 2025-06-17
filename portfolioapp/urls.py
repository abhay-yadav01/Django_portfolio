from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('header/', views.header, name='header'),
    path('about/', views.about_me, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('education/', views.education, name='education'),
    path('feedback/', views.feedback_form, name='feedback'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
]


# urlpatterns += static(settings.MEDIA_URL, documents_root = settings.MEDIA_URL)
# urlpatterns += static(settings.STATIC_URL, documents_root = settings.STATIC_ROOT)
