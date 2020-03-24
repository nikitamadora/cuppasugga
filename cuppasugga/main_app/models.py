from django.db import models
from django.db.models import CharField
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'profile {self.id}' 
    # If True, the field is allowed to be blank. Default is False
    # bag = models.ForeignKey(Bag, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def user_bags(self):
        return self.bag_set.filter(user=user)

# User profile can have one bag (MVP) --> can expand to many later
class Bag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    # donor_email = models.EmailField(max_length=50)
    
    def __str__(self):
      return f'bag {self.id}'