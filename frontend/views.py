from django.shortcuts import render

from api.models import Profile

def MainView(request):
    profile = Profile.objects.get(id=1)
    context = {'profile': profile}
    return render(request, 'frontend/index.html', context)
