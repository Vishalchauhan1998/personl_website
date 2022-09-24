from django.shortcuts import render
from .models import Profile
# Create your views here.

def profiles(request):
    prodata = Profile.objects.all()
    #print("Data is--->", prodata)
    context = {'pro':prodata}
    return render(request, 'base/navbar.html', context)
