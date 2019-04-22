from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Image, HashTag
from .forms import PostModelForm, ImageModelForm, CommentModelForm
from IPython import embed


@login_required
@require_http_methods(['GET', 'POST'])
def create_post(request):
    if request.method == 'POST':
        # ModelForm(data, files)
        post_form = PostModelForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

            # create hashtag
            content = post_form.cleaned_data.get('content')  #
            words = content.split(' ')  # 띄어쓰기 기준으로 split
            for word in words:
                if word[0] == '#':
                    word = word[1:]
                    tag = HashTag.objects.get_or_create(content=word)  # (HashTagObj, T/F)
                    post.tags.add(tag[0])
                    if tag[1]:  # tag 가 처음 만들어 진거라면, 메세지 추가!
                        messages.add_message(
                            request,
                            messages.SUCCESS,
                            f'#{tag[0].content} 태그 를 처음으로 추가하셨어요! :)'
                        )

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
    # 지금 수정하려는 post 작성자가 요청 보낸 사람이냐?
    if post.user == request.user:
        if request.method == 'POST':
            post_form = PostModelForm(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                # update hashtag
                post.tags.clear()  # 기존의 tag 다 날리기!
                content = post_form.cleaned_data.get('content')  #
                words = content.split(' ')  # 띄어쓰기 기준으로 split
                for word in words:
                    if word[0] == '#':
                        word = word[1:]
                        tag = HashTag.objects.get_or_create(content=word)  # (HashTagObj, T/F)
                        post.tags.add(tag[0])
                return redirect('posts:post_list')
        else:
            post_form = PostModelForm(instance=post)

        return render(request, 'posts/form.html', {
            'post_form': post_form
        })
    else:  # 작성자와 요청 보낸 user 가 다르다면,
        # 403 : Forbidden 금지됨!
        return redirect('posts:post_list')


@require_GET
def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
    })


@login_required
@require_POST
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentModelForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
        # TODO: else => if comment is not valid, then what?


@login_required
@require_POST
def toggle_like(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    # if post.like_users.filter(id=user.id).exists():  # 찾으면, [value] / 없으면, []
    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:post_list')


@require_GET
def tag_posts_list(request, tag_name):
    tag = get_object_or_404(HashTag, content=tag_name)
    posts = tag.posts.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
        'h1': f'#{tag} 를 포함한 posts 입니다.'
    })
