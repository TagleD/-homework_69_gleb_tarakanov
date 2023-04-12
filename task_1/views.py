import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def add_view(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        try:
            response = JsonResponse({
                'answer': int(data['A']) + int(data['B'])
            })
        except ValueError:
            response_data = {'error': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


@require_http_methods(['GET'])
def subtract_view(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        try:
            response = JsonResponse({
                'answer': int(data['A']) - int(data['B'])
            })
        except ValueError:
            response_data = {'error': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


@require_http_methods(['GET'])
def multiply_view(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        try:
            response = JsonResponse({
                'answer': int(data['A']) * int(data['B'])
            })
        except ValueError:
            response_data = {'error': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


@require_http_methods(['GET'])
def divide_view(request, *args, **kwargs):
    if request.body:
        data = json.loads(request.body)
        try:
            response = JsonResponse({
                'answer': int(data['A']) / int(data['B'])
            })
        except ValueError:
            response_data = {'error': 'Некорректный набор данных'}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response
