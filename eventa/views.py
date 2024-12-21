# views.py
from django.shortcuts import render

def home(request):
    # You can pass context to the template
    context = {'message': 'Welcome to the site!'}
    return render(request, '/front-end/index.html', context)
