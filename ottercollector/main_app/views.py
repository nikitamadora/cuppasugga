from django.shortcuts import render, redirect
from .models import Otter, Toy
from .forms import OtterForm, FeedingForm, ToyForm

# Create your views here.

# views for otters
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def otters_index(request):
    otters = Otter.objects.all()
    return render(request, 'otters/index.html', { 'otters' : otters })

def otters_detail(request, otter_id):
    otter = Otter.objects.get(id=otter_id)
    toys_otter_doesnt_have = Toy.objects.exclude(id__in = otter.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'otters/detail.html', { 
        'otter': otter, 'feeding_form': feeding_form,
        'toys': toys_otter_doesnt_have
    })

def add_feeding(request, otter_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.otter_id = otter_id
        new_feeding.save()
    return redirect('detail', otter_id=otter_id)

def assoc_toy(request, otter_id, toy_id):
    Otter.objects.get(id=otter_id).toys.add(toy_id)
    return redirect('detail', otter_id=otter_id)

def del_assoc_toy(request, otter_id, toy_id):
    Otter.objects.get(id=otter_id).toys.remove(toy_id)
    return redirect('detail', otter_id=otter_id)

def new_otter(request):
    if request.method == 'POST':
        form = OtterForm(request.POST)
        if form.is_valid():
            otter = form.save()
            return redirect('detail', otter.id)
    else:
        form = OtterForm()
    context = { 'form': form }
    return render(request, 'otters/otter_form.html', context)

# views for toys
def toys_index(request):
    toys = Toy.objects.all()
    print(toys)
    return render(request, 'main_app/toy_list.html', { 'toys': toys })

def toys_detail(request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    return render(request, 'main_app/toy_detail.html', { 'toy': toy })

def toys_update(request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    form = ToyForm(request.POST or None, instance = toy)
    if form.is_valid():
        upd_toy = form.save()
        return redirect('toys_index')
    else:
        form = ToyForm()
    context = { 'form': form }
    return render(request, 'main_app/toy_form.html', context)

def toys_create(request):
    if request.method == 'POST':
        form = ToyForm(request.POST)
        if form.is_valid():
            toy = form.save()
            return redirect('toys_detail', toy.id)
    else:
        form = ToyForm()
    context = { 'form': form }
    return render(request, 'main_app/toy_form.html', context)

def toys_delete(request, toy_id):
    context = {}
    toy = Toy.objects.get(id=toy_id)
    if request.method == 'POST':
        toy.delete()
        return redirect('toys_index')

    return render(request, 'main_app/toy_confirm_delete.html', context)
    # render(request, 'main_app/toy_confirm_delete.html')

    # if request.method == 'POST':
    #     toy.delete()
    #     return redirect('toys_detail', toy.id)
    # else:
    #     form = ToyForm()
    # context = { 'form': form }
    # return render(request, 'main_app/toy_form.html', context)