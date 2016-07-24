# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def home(request):
    params = {}
    if request.user.is_authenticated():
        params['userapps'] = UserApps.objects.filter(user=request.user, status=True).order_by('app')
    return render(request, 'home.html', params)

@login_required
def edit_home(request):
    params = {}
    if request.user.is_authenticated():
          params['userapps'] = UserApps.objects.filter(user=request.user).order_by('app')
          if request.method=='POST':
              for ua in params['userapps']:
                  appselected = request.POST.get(ua.app.name, False)
                  ua.status = appselected
                  ua.save()
              return redirect('home')            
    return render(request, 'edit_home.html', params)

