from boto3 import session
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
import boto3
from boto3.session import Session
from decouple import config
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")

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
        message = f"From: {data['email']} \n\nHello my name is: {data['name']} \n{data['body']}"
        send_mail(
            data['subject'],
            message,
            data['email'],
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

    return render(request, 'frontend/email.html', {'form': form})


def ResumeDL(request):
    # session = Session(aws_access_key_id=config('AWS_ACCESS_KEY_ID'), aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'))

    # session.resource('s3').Bucket('static-port').download_file('media/resume/Resume.png', '/Users/Kyrios/Desktop/Resume.png')
    s3 = boto3.client('s3', aws_access_key_id=config('AWS_ACCESS_KEY_ID'), aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'))
    with open(downloads_path + '/Resume.pdf', 'wb') as f:
        s3.download_fileobj('static-port', 'media/resume/Resume.pdf', f)

    return redirect('index')