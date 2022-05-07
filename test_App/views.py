from django.shortcuts import render
from test_App.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'Registration/registration.html')
@csrf_exempt
def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['firstname'], last_name=request.POST['lastname'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')
def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'Registration/success.html', context)  
def login(request):  
    return render(request, 'Login/login.html')