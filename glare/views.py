from django.shortcuts import render_to_response

# Create your views here.


def home(request):
    return render_to_response('glare/home.html')


def profile(request):
    return render_to_response('glare/profile.html')
