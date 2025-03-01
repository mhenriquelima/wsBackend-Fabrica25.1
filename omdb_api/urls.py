from django.urls import path
from .views import movieView, movieListView, movieDetail, movieDeleteView, movieUpdateView, sign_in, error

app_name = 'omdb_api'

urlpatterns = [
    path('search/', movieView.as_view(), name='search'),
    path('list/', movieListView.as_view(), name='list'),
    path('detail/<int:pk>/', movieDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', movieDeleteView.as_view(), name='delete'),
    path('error/', error, name='error'),
    path('update/<int:pk>/', movieUpdateView.as_view(), name='update'),
]
