from django import forms
from .models import Bag

# Bag
class BagForm(forms.ModelForm):
    class Meta:
        model = Bag
        fields = ('content',)

# Items
# class FeedingForm(forms.ModelForm):
#     class Meta:
#         model = Feeding
#         fields = ['date', 'meal']

# Items
# class ToyForm(forms.ModelForm):
#     class Meta:
#         model = Toy
#         fields = ('name', 'color')