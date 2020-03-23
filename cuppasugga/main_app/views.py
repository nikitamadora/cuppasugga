from django.shortcuts import render, redirect
from .models import User, Profile, Bag
from .forms import BagForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# user signup view
def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('public_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context )

# Landing Page
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def public_index(request):
    bags = Bag.objects.all()
    return render(request, 'bags/index.html', { 'bags' : bags })

@login_required
def new_bag(request):
    if request.method == 'POST':
        form = BagForm(request.POST)
        if form.is_valid():
            bag = form.save(commit=False)
            bag.user = request.user
            # built in auth automatically assigns user to request
            bag.save()
            return redirect('public_index')
    else:
        form = BagForm()
    context = { 'form': form }
    return render(request, 'bags/bag_form.html', context)


# @login_required
def public_bag_detail(request, bag_id):
    bag = Bag.objects.get(id=bag_id)
    return render(request, 'bags/public_detail.html', { 'bag' : bag })


###### PROFILE VIEWS
def profile(request):
    user = request.user
    bags = Bag.objects.filter(user=user)
    return render(request, 'main_app/profile.html', {'bags': bags})

def profile_bag_detail(request, user_id, bag_id):
    user_id = User.objects.get(id=user_id)
    bag = Bag.objects.get(id=bag_id)

    return render(request, 'main_app/bag_detail.html', {'bag': bag}) 

# @login_required
def bags_update(request, user_id, bag_id):
    user_id = User.objects.get(id=user_id)
    bag = Bag.objects.get(id=bag_id)
    if request.method == 'POST':
        form = BagForm(request.POST, instance=bag)
        if form.is_valid():
            bag = form.save()
            return redirect('profile')
    else:
        form = BagForm(instance=bag)
    context = { 'form': form }
    return render(request, 'main_app/update_bag_form.html', context)
   
# @login_required
def bags_delete(request, user_id, bag_id):
    context = {}
    user_id = User.objects.get(id=user_id)
    bag = Bag.objects.get(id=bag_id)
    if request.method == 'POST':
        bag.delete()
        return redirect('profile')

    return render(request, 'main_app/bag_confirm_delete.html', context)


# def update_submit(request, bag_id):
#     if request.method == 'POST':
#         form = UpdateForm(request.POST, instance=bag)
#         if form.is_valid():
#             bag = form.save()
#             return redirect('profile')
#     else:
#         form = UpdateForm(instance=bag)
#     context = { 'form': form }
#     return render(request, 'main_app/update_bag_form.html', context)



# @login_required
# def add_item(request, bag_id):
#     form = ItemForm(request.POST)
#     if form.is_valid():
#         new_item = form.save(commit=False)
#         new_item.otter_id = otter_id
#         new_item.save()
#     return redirect('detail', otter_id=otter_id)

# @login_required
# def assoc_toy(request, otter_id, toy_id):
#     Otter.objects.get(id=otter_id).toys.add(toy_id)
#     return redirect('detail', otter_id=otter_id)

# @login_required
# def del_assoc_toy(request, otter_id, toy_id):
#     Otter.objects.get(id=otter_id).toys.remove(toy_id)
#     return redirect('detail', otter_id=otter_id)

# 
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