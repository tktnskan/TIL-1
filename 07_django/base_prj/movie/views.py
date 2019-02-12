from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from IPython import embed

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/list.html', {
        'movies': movies
    })

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            title_eng = form.cleaned_data.get('title_eng')
            audience = form.cleaned_data.get('audience')
            open_date = form.cleaned_data.get('open_date')
            genre = form.cleaned_data.get('genre')
            watch_grade = form.cleaned_data.get('watch_grade')
            score = form.cleaned_data.get('score')
            # embed()
            poster_url = form.cleaned_data.get('poster_url')
            description = form.cleaned_data.get('description')

            Movie.objects.create(
                title=title, title_eng=title_eng, audience=audience,
                open_date=open_date, genre=genre, watch_grade=watch_grade,
                score=score, poster_url=poster_url, description=description,
            )
            return redirect('movie:list')
    else:
        form = MovieForm()

    return render(request, 'movie/create.html', {
        'form': form,
    })
