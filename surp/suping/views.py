
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import registerForm, loginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FileUpload

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        file_upload = FileUpload(file=uploaded_file)
        file_upload.save()
        saved_filename = file_upload.file.name
        return JsonResponse({'message': 'File uploaded and saved successfully!', 'saved_filename': saved_filename})
    else:
        return JsonResponse({'message': 'Invalid request method'})


def indexView(request):
    context = {}
    return render(request, 'index.html', context)

def RegisterView(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if User.objects.filter(username=username).exists():
                form.errors['username'] = [
                    'Username is allready taken by someone, try another']
            elif User.objects.filter(email=email).exists():
                form.errors['username'] = [f'{email} is allready signed-up']
            elif password != password2:
                form.errors['username'] = ['passwords does not match']
            else:
                user = form.save(commit=False)
                user.set_password(password)
                form.save()
                login(request, user)
                return redirect('index')
    else:
        form = registerForm()
    return render(request, 'register.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                username = user.username
                userAuth = authenticate(
                    request, username=username, password=password)
                if userAuth is not None:
                    login(request, user)
                    return redirect('index')
            except:
                form.errors['username'] = ['Invalid username or password']
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form})


def logoutView(request):
    logout(request)
    return redirect('login')

