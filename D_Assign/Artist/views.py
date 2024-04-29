from django.shortcuts import render, redirect
from .forms import UserReg
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserReg()
    return render(request, 'register.html', {'form' : form})

@login_required
def home(request):
    return render(request, 'home.html')

def get_token(request):
    tok, create = Token.objects.get_or_create(user=request.user)
    return render(request, 'home.html', {'tok':tok})