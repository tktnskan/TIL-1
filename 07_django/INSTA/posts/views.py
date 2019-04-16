from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Post
from .forms import PostModelForm


@require_http_methods(['GET', 'POST'])
def create_post(request):
    # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
    if request.method == 'POST':
        # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
        form = PostModelForm(request.POST, request.FILES)

        if form.is_valid():  # Data 검증을 한다.
            # 통과하면 저장한다.
            form.save()
            # 저장하고, redirect
            return redirect('posts:post_list')
        else:
            # 실패하면, 다시 data 입력 form 을 준다.
            pass
    # GET 방식으로 요청이 오면,
    else:
        # 새로운 Post 용 form 을 만든다.
        form = PostModelForm()
    # 사용자에게 html 과 form 을 같이 넘긴다.
    return render(request, 'posts/form.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
        else:
            pass
    else:
        form = PostModelForm(instance=post)
    return render(request, 'posts/form.html', {
        'form': form
    })


@require_GET
def post_list(request):
    posts = Post.objects.all()

    return render(request, 'posts/list.html', {
        'posts': posts,
    })
