from django.shortcuts import render, redirect
from .models import Profile, Bag, Item
from .forms import BagForm, ItemForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# user signup view
# def signup(request):
#     error_message=''
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#         else:
#             error_message = 'Invalid sign up - try again'
#     form = UserCreationForm()
#     context = { 'form': form, 'error_message': error_message }
#     return render(request, 'registration/signup.html', context )

# views for otters
# def home(request):
#     return render(request, 'home.html')

# def about(request):
#     return render(request, 'about.html')

# @login_required
# def otters_index(request):
#     otters = Otter.objects.filter(user=request.user)
#     return render(request, 'otters/index.html', { 'otters' : otters })

# @login_required
# def otters_detail(request, otter_id):
#     otter = Otter.objects.get(id=otter_id)
#     toys_otter_doesnt_have = Toy.objects.exclude(id__in = otter.toys.all().values_list('id'))
#     feeding_form = FeedingForm()
#     return render(request, 'otters/detail.html', { 
#         'otter': otter, 'feeding_form': feeding_form,
#         'toys': toys_otter_doesnt_have
#     })

# @login_required
def add_item(request, bag_id):
    form = ItemForm(request.POST)
    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.otter_id = otter_id
        new_item.save()
    return redirect('detail', otter_id=otter_id)

# @login_required
# def assoc_toy(request, otter_id, toy_id):
#     Otter.objects.get(id=otter_id).toys.add(toy_id)
#     return redirect('detail', otter_id=otter_id)

# @login_required
# def del_assoc_toy(request, otter_id, toy_id):
#     Otter.objects.get(id=otter_id).toys.remove(toy_id)
#     return redirect('detail', otter_id=otter_id)

# @login_required
# def new_otter(request):
#     if request.method == 'POST':
#         form = OtterForm(request.POST)
#         if form.is_valid():
#             otter = form.save(commit=False)
#             otter.user = request.user
#             # built in auth automatically assigns user to request
#             otter.save()
#             return redirect('detail', otter.id)
#     else:
#         form = OtterForm()
#     context = { 'form': form }
#     return render(request, 'otters/otter_form.html', context)

# # views for toys
# @login_required
# def toys_index(request):
#     toys = Toy.objects.all()
#     print(toys)
#     return render(request, 'main_app/toy_list.html', { 'toys': toys })

# @login_required
# def toys_detail(request, toy_id):
#     toy = Toy.objects.get(id=toy_id)
#     return render(request, 'main_app/toy_detail.html', { 'toy': toy })

# @login_required
# def toys_create(request):
#     if request.method == 'POST':
#         form = ToyForm(request.POST)
#         if form.is_valid():
#             toy = form.save()
#             return redirect('toys_detail', toy.id)
#     else:
#         form = ToyForm()
#     context = { 'form': form }
#     return render(request, 'main_app/toy_form.html', context)

# @login_required
# def toys_update(request, toy_id):
#     toy = Toy.objects.get(id=toy_id)
#     if request.method == 'POST':
#         form = ToyForm(request.POST, instance=toy)
#         if form.is_valid():
#             toy = form.save()
#             return redirect('toys_index')
#     else:
#         form = ToyForm(instance=toy)
#     context = { 'form': form }
#     return render(request, 'main_app/toy_form.html', context)

# @login_required
# def toys_delete(request, toy_id):
#     context = {}
#     toy = Toy.objects.get(id=toy_id)
#     if request.method == 'POST':
#         toy.delete()
#         return redirect('toys_index')

#     return render(request, 'main_app/toy_confirm_delete.html', context)