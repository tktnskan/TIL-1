from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Post, Image
from .forms import PostModelForm, ImageModelForm


@require_http_methods(['GET', 'POST'])
def create_post(request):
    if request.method == 'POST':
        post_form = PostModelForm(request.POST)
        if post_form.is_valid():
            post = post_form.save()
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageModelForm(request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('posts:post_list')
        else:
            pass
    else:
        post_form = PostModelForm()
        image_form = ImageModelForm()
    return render(request, 'posts/form.html', {
        'post_form': post_form,
        'image_form': image_form,
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
