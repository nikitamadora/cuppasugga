from django import forms
from .models import Otter, Feeding, Toy

class OtterForm(forms.ModelForm):
    class Meta:
        model = Otter
        fields = ('name', 'species', 'description', 'age')

class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']

class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ('name', 'color')