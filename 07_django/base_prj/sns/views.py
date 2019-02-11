from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment

def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'sns/list.html', {
        'postings': postings,
    })

def posting_detail(request):
    pass

def create_posting(request):
    pass

def edit_posting(request):
    pass

def delete_posting(request):
    pass
