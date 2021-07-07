from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView, name="index"),
    path('send_email/submit/', views.SendEmail, name='send_email'),
    path('resume_download/', views.ResumeDL, name="resume_dl"),
]
