from django import forms
from .models import Otter, Feeding, Toy

# Bag
class OtterForm(forms.ModelForm):
    class Meta:
        model = Otter
        fields = ('name', 'species', 'description', 'age')

# Items
# class FeedingForm(forms.ModelForm):
#     class Meta:
#         model = Feeding
#         fields = ['date', 'meal']

# Items
class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = ('name', 'color')