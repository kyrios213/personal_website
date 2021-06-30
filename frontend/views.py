from django.shortcuts import render

from api.models import Profile, Projects

def MainView(request):
    profile = Profile.objects.get(id=1)
    projects = Projects.objects.all()
    
    context = {
        'profile': profile,
        'projects': projects
        }
    return render(request, 'frontend/index.html', context)
