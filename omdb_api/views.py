from django.shortcuts import redirect, render
from django.views.generic import FormView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

from .models import movieModel, Review
from .forms import movieForm, ReviewForm

import requests

class movieView(FormView):
    template_name = 'omdb_api/search.html'
    form_class = movieForm
    success_url = reverse_lazy('omdb_api:list')
    failure_url = reverse_lazy('omdb_api:error')

    def form_valid(self, form):
        title = form.cleaned_data['title']
        url = f'http://www.omdbapi.com/?t={title}&apikey=4a3b711b'
        response = requests.get(url)
        if response.status_code == 200:
            movie = response.json()
            if movie.get('Response') == 'True':
                movieModel.objects.create(
                    title=movie.get('Title', 'N/A'),
                    year=movie.get('Year', 'N/A'),
                    type=movie.get('Type', 'N/A'),
                    genre=movie.get('Genre', 'N/A'),
                    director=movie.get('Director', 'N/A'),
                    writer=movie.get('Writer', 'N/A'),
                    actors=movie.get('Actors', 'N/A'),
                    awards=movie.get('Awards', 'N/A'),
                    rating=movie['Ratings'][0]['Value'] if movie.get('Ratings') else 'N/A'
                )
                return super().form_valid(form)
        return HttpResponseRedirect(self.failure_url)
    
class movieListView(ListView):
    model = movieModel
    template_name = 'omdb_api/list.html'
    context_object_name = 'movies'
    
class movieDetail(DetailView):
    model = movieModel
    template_name = 'omdb_api/detail.html'
    context_object_name = 'movie'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = self.object
            review.save()
            return redirect('omdb_api:detail', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))

class movieDeleteView(DeleteView):
    model = movieModel
    template_name = 'omdb_api/delete.html'
    success_url = reverse_lazy('omdb_api:list')
    
class movieUpdateView(UpdateView):
    model = movieModel
    template_name = 'omdb_api/update.html'
    success_url = reverse_lazy('omdb_api:list')
    fields = ['title', 'year', 'type', 'genre', 'director', 'writer', 'actors', 'awards', 'rating']
    
def error(request):
    return render(request, 'omdb_api/error.html')