from django.shortcuts import render
from .models import Otter
# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello, you really otter be my friend</h1>')

def about(request):
    return render(request, 'about.html')

def otters_index(request):
    otters = Otter.objects.all()
    return render(request, 'otters/index.html', { 'otters' : otters })

def otters_detail(request, otter_id):
  otter = Otter.objects.get(id=otter_id)
  return render(request, 'otters/detail.html', { 'otter': otter})