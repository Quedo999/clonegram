from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

def main(request):
    if request.method == 'GET':
        return render(request, 'users/main.html')
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # 로그인 성공 시 포스트 앱으로 리다이렉트
            return HttpResponseRedirect(reverse('posts:index'))
        else:
            # 로그인 실패 시 다시 메인화면으로
            return render(request, 'users/main.html')

def signup(request):
    if request.method == 'GET':
        form = SignUpForm()

        return render(request, 'users/signup.html', {'form': form})

    elif request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # 로그인 성공 시 포스트 앱으로 리다이렉트
                return HttpResponseRedirect(reverse('posts:index'))
            
        return render(request, 'users/main.html')
