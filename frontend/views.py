from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from api.models import Profile, Projects
from .forms import SendEmailForm

def MainView(request):
    profile = Profile.objects.get(id=1)
    projects = Projects.objects.all()
    
    context = {
        'profile': profile,
        'projects': projects
        }
    return render(request, 'frontend/index.html', context)


def SendEmail(request):
    form = SendEmailForm
    if request.method == 'POST':
        data = request.POST
        message = f"From: {data['email']} \n\n{data['body']}"
        send_mail(
            data['subject'],
            message,
            data['email'],
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

    return render(request, 'frontend/email.html', {'form': form})
