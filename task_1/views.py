import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            try:
                answer = int(data['A']) + int(data['B'])
                return JsonResponse({'answer': answer}, status=200)
            except:
                answer = 'Not valid input'
                return JsonResponse({'answer': answer}, status=400)
        else:
            return JsonResponse({'answer': 'Not valid input'}, status=400)
    else:
        return JsonResponse({'answer': 'Not valid method'}, status=400)


@csrf_exempt
def subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            try:
                answer = int(data['A']) - int(data['B'])
                return JsonResponse({'answer': answer}, status=200)
            except:
                answer = 'Not valid input'
                return JsonResponse({'answer': answer}, status=400)
        else:
            return JsonResponse({'answer': 'Not valid input'}, status=400)
    else:
        return JsonResponse({'answer': 'Not valid method'}, status=400)


@csrf_exempt
def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            try:
                answer = int(data['A']) * int(data['B'])
                return JsonResponse({'answer': answer}, status=200)
            except:
                answer = 'Not valid input'
                return JsonResponse({'answer': answer}, status=400)
        else:
            return JsonResponse({'answer': 'Not valid input'}, status=400)
    else:
        return JsonResponse({'answer': 'Not valid method'}, status=400)


@csrf_exempt
def divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            data = json.loads(request.body)
            try:
                answer = int(data['A']) / int(data['B'])
                return JsonResponse({'answer': answer}, status=200)
            except:
                answer = 'Not valid input'
                return JsonResponse({'answer': answer}, status=400)
        else:
            return JsonResponse({'answer': 'Not valid input'}, status=400)
    else:
        return JsonResponse({'answer': 'Not valid method'}, status=400)
