# Create your views here.
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import templates
from django.views.decorators.csrf import csrf_exempt

from .models import Ranking
from sudoku.sudoku import Sudoku

import json
import datetime

def main(request):
    return render(request, 'main.html')

@csrf_exempt
def index(request):
    context = {}
    return render(request, 'index.html', context)

def explain(request):
    context = {}
    return render(request, 'explain.html', context)

def make_sudoku(request):
    sudoku_api = Sudoku()
    board = sudoku_api.generate_puzzle()
    result = {
        'board': board
    }
    return JsonResponse(result)

def check_sudoku(request):
    sudoku_api = Sudoku()
    request_data = json.loads(request.body)

    if 'puzzle' not in request_data or 'elapsed_time' not in request_data:
        JsonResponse({'status': 'fail'})

    puzzle = request_data['puzzle']
    elapsed_time = request_data['elapsed_time']

    result = sudoku_api.check_answer(puzzle)
    data = {}
    if result:
        data['status'] = 'clear'
        request.session['status'] = 'clear'
        request.session['elapsed_time'] = elapsed_time
    else:
        data['status'] = 'fail'
    return JsonResponse(data)

def ranking(request):
    context = {}
    return render(request, 'ranking.html', context)

def get_ranking_list(request):
    ranking_list = Ranking.objects.order_by('elapsed_time')[:10]
    ranking_data = serializers.serialize('json', ranking_list, fields=('name', 'elapsed_time'))
    ranking_data = json.loads(ranking_data)
    ranking_data = [{**item['fields'], **{'pk': item['px']}} for item in ranking_data]
    ranking_data = {
        'data': ranking_data
    }
    return JsonResponse(ranking_data)

def register_ranking(request):
    if 'elapsed_time' not in request.session:
        return JsonResponse({'status': 'failed'})

    data = json.loads(request.body)
    name = data['name']
    elapsed_time = request.session['elapsed_time']

    datetime_args = elapsed_time // 3600, (elapsed_time % 3600) // 60, elapsed_time % 60
    d = datetime.time(datetime_args[0], datetime_args[1], datetime_args[2])

    ranking = Ranking(name=name, elapsed_time=d)
    ranking.save()

    return JsonResponse({'status': 'success'})


