from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def hello(request):
    data = {}
    data['say'] = 'hello'
    response = {
        'status': 'OK',
        'error': '',
        'data': data
    }
    return JsonResponse(response)
