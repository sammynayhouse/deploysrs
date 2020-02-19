from django.shortcuts import render
from .models import Genre, Movie
# Create your views here.
def index(request):
    genre_list = Genre.objects.all()
    return render(request, 'week2_app/index.html', {'genres':genre_list})

def about(request):
    return render(request, 'week2_app/about.html')