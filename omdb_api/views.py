from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from django.urls import reverse_lazy

from .models import movieModel
from .forms import movieForm

import requests

# Create your views here.
class movieView(FormView):
    template_name = 'omdb_api/search.html'
    form_class = movieForm
    success_url = reverse_lazy('omdb_api:list')

    def form_valid(self, form):
        title = form.cleaned_data['title']
        url = f'http://www.omdbapi.com/?t={title}&apikey=4a3b711b'
        response = requests.get(url)
        if response.status_code == 200:
            movie = response.json()
            movieModel.objects.create(
                title = movie['Title'],
                year = movie['Year'],
                type = movie['Type'],
                genre = movie['Genre'],
                director = movie['Director'],
                writer = movie['Writer'],
                actors = movie['Actors'],
                awards = movie['Awards'],
                rating = movie['Ratings'][0]['Value']
            )
        else:
            print('Error cannot find movie')
        return super().form_valid(form)
    
class movieListView(ListView):
    model = movieModel
    template_name = 'omdb_api/list.html'
    context_object_name = 'movies'
    
class movieDetail(DetailView):
    model = movieModel
    template_name = 'omdb_api/detail.html'
    context_object_name = 'movie'