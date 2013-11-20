from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse


def home(request):
    if request.user.is_authenticated():
        return redirect('/profile')  # reverse('glare.views.profile'))
    return render_to_response('glare/home.html')


def profile(request):
    return render_to_response('glare/profile.html')
