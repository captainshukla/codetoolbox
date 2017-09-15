from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
import requests

def homepage(request):
    return render(request, "index.html", {})


def check_code(request):
    RUN_URL = u'http://api.hackerearth.com/code/run/'
    CLIENT_SECRET = 'b4a1adb105a03b0f32a3e1813f55a27c93053802'

    source = "print('Vishal')"

    constraint = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': source,
        'lang': "PYTHON",
        'time_limit': 5,
        'memory_limit': 262144,
    }

    r = requests.post(RUN_URL, data=constraint)
    x = r.json()

    for key in x:
        if key == 'web_link':
            code_url = x[key]
        if key == 'run_status':
            for j in x[key]:
                if j == "output":
                    output = x[key][j]

    data = {
        'url': code_url,
        'output': output,
    }
    return JsonResponse(data)