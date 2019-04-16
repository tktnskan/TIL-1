from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Post, Image
from .forms import PostModelForm, ImageModelForm
from IPython import embed


@login_required
@require_http_methods(['GET', 'POST'])
def create_post(request):
    if request.method == 'POST':
        # ModelForm(data, files)
        post_form = PostModelForm(request.POST)
        if post_form.is_valid():
            post = post_form.save()
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageModelForm(files=request.FILES)
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


@login_required
@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostModelForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:post_list')
        else:
            pass
    else:
        post_form = PostModelForm(instance=post)
    return render(request, 'posts/form.html', {
        'post_form': post_form
    })


@require_GET
def post_list(request):

    posts = Post.objects.all()

    return render(request, 'posts/list.html', {
        'posts': posts,
    })
#
# def post_detail(request):
#     post = get_object_or_404(Post, id=1)
#
#     return render(request, 'posts/deatil.html', {
#         'post': post,
#         'images': post.image_set.all()
#     })
