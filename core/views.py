from django.shortcuts import redirect, render
from .forms import SingUpForm

from django.contrib.auth import login

# Create your views here.


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            
            return redirect('home')
        
    else:
        form = SingUpForm()
        
    context = {
        'form':form,
    }
        
    return render(request, 'signup.html', context)
