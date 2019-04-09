from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Posting, Comment
from IPython import embed

# Create
@require_http_methods(['GET', 'POST'])
def create_posting(request):
    if request.method == 'POST':
        posting = Posting()
        posting.title = request.POST.get('title')  # None
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board_ad:posting_detail', posting_id=posting.id)  # articles/??
    else:
        return render(request, 'board_ad/new.html')

# Read
@require_http_methods(['GET'])
def posting_list(request):
    postings = Posting.objects.all()
    # postings = get_list_or_404(Posting)  # res => 404
    return render(request, 'board_ad/list.html', {
        'postings': postings,
    })

@require_http_methods(['GET'])
def posting_detail(request, posting_id):
    # posting = Posting.objects.get(id=id)
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all()
    return render(request, 'board_ad/detail.html', {
        'posting': posting,
        'comments': comments,
    })

# Update
@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == 'POST':
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board_ad:posting_detail', posting_id=posting.id)
    else:
        return render(request, 'board_ad/edit.html', {
            'posting': posting,
        })

# Delete
@require_http_methods(['POST'])
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('board_ad:posting_list')


@require_http_methods(['POST'])
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = Comment()
    comment.posting = posting
    comment.content = request.POST.get('comment')
    comment.save()
    return redirect('board_ad:posting_detail', posting_id)


@require_http_methods(['POST'])
def delete_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()

    return redirect('board_ad:posting_detail', posting_id=posting.id)
