from django.shortcuts import render, redirect
from .models import Movie
from IPython import embed

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/list.html', {
        'movies': movies
    })

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        title_eng = request.POST.get('title_eng')
        audience = int(request.POST.get('audience'))
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = float(request.POST.get('score'))
        # embed()
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')

        Movie.objects.create(
            title=title, title_eng=title_eng, audience=audience,
            open_date=open_date, genre=genre, watch_grade=watch_grade,
            score=score, poster_url=poster_url, description=description,
        )

        return redirect('movie:list')
    else:
        return render(request, 'movie/create.html')
