from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from IPython import embed


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('posts:post_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    # 우선, 사용자가 로그인 되어 있는지?
    if request.user.is_authenticated:
        return redirect('posts:post_list')
    else:  # 로그인 안 되어 있다면,
        if request.method == 'POST':  # 사용자가 로그인 데이터를 넘겼을 때
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect(request.GET.get('next') or 'posts:post_list')
        else:  # 사용자가 로그인 화면을 요청할 때
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {
            'form': form
        })


def logout(request):
    auth_logout(request)
    return redirect('posts:post_list')

