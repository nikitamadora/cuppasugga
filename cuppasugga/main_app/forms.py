from django import forms
from django.forms import ValidationError
from .models import Bag, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import NON_FIELD_ERRORS


class BagForm(forms.ModelForm):
    class Meta:
        # error_messages = {
        #     NON_FIELD_ERRORS:{
        #         'character_max': '%(model_name)s% (field_label)s has a 50 character limit'
        #     }
        # }
        model = Bag
        fields = ('name','content')


# return alphanumeric and whitespace values; no special chars
    def clean_name(self):
        name = self.cleaned_data['name']

        if name.isprintable():
            return name
        raise ValidationError("Bag name can only be one word. Please try again")
    
# alphanumeric, whitespace, and commas only; no other special chars
    def clean_content(self):
        content = self.cleaned_data['content']
        if content.isprintable():
            return content
        raise ValidationError("can only use letters, numbers, or ','s. please try again ")

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'bio')
