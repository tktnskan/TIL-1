from django.shortcuts import render, redirect
from .models import Writer, Book, Chapter
from .forms import *


def create(request):
    if request.method == 'POST':
        form = WriterModelForm(request.POST)
        if form.is_valid():  # request.POST 에 있는 data 저장가능??
            form.save()
            return redirect('detail')
        else:  # 실패하면?
            pass

    elif request.method == 'GET':
        form = WriterModelForm()

    return render(request, 'new.html', {
        'form': form,
    })


def update(request, id):
    writer = Writer.objects.get(id=id)

    if request.method == 'POST':
        form = WriterModelForm(request.POST, instance=writer)
        if form.is_valid():
            form.save()
            return redirect('detail')
        else:
           pass

    elif request.method == 'GET':
        form = WriterModelForm(instance=writer)

    return render(request, 'edit.html', {
        'form': form
    })