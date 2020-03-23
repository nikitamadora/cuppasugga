from django import forms
from .models import Bag

# Bag
class BagForm(forms.ModelForm):
    class Meta:
        model = Bag
        fields = ('name','content')


# class UpdateForm(forms.ModelForm):
#     class Meta:
#         model = Bag
#         fields =  ('content',)

# Items
# class ToyForm(forms.ModelForm):
#     class Meta:
#         model = Toy
#         fields = ('name', 'color')