from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('sudoku/index', views.index, name='index'),
    path('sudoku/make', views.make_sudoku, name='make_sudoku'),
    path('sudoku/check', views.check_sudoku, name='check_sudoku'),
    path('sudoku/ranking', views.ranking, name='ranking'),
    path('ranking', views.ranking, name='ranking'),
    path('sudoku/ranking', views.get_ranking_list, name='get_ranking_list'),
    path('sudoku/ranking/register', views.register_ranking, name='register_ranking'),
    path('sudoku/explain', views.explain, name='explain'),
]