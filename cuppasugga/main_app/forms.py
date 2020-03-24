from django import forms
from .models import Bag, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BagForm(forms.ModelForm):
    class Meta:
        model = Bag
        fields = ('name','content')

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'bio')
