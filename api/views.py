from django.shortcuts import render

from .models import Profile

def test(request):
    profile = Profile.objects.get(pk=1)
    context = {
        'profile': profile,
    }
    return render(request, 'index.html', context)