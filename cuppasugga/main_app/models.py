from django.db import models
from django.db.models import CharField
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'profile {self.id}' 
    # If True, the field is allowed to be blank. Default is False
    # bag = models.ForeignKey(Bag, on_delete=models.CASCADE)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# User profile can have one bag (MVP) --> can expand to many later
class Bag(models.Model):
    # item = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
      return f'bag {self.id}' 

   
# class Item(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(max_length=200)
#     quantity = models.PositiveSmallIntegerField()
#     bag = models.ForeignKey(Bag, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Toy(models.Model):
#     name = models.CharField(max_length=50)
#     color = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

# class Otter(models.Model):
#     name = models.CharField(max_length=100)
#     species = models.CharField(max_length=100)
#     description = models.TextField(max_length=250)
#     age = models.IntegerField()
#     toys = models.ManyToManyField(Toy)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    
#     def fed_for_today(self):
#         return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

# class Feeding(models.Model):
#     date = models.DateField('feeding date')
#     meal = models.CharField(
#         max_length=1,
#         choices=MEALS,
#             default=MEALS[0][0]
#     )
    
#     otter = models.ForeignKey(Otter, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.get_meal_display()} on {self.date}'
    
#     class Meta:
#         ordering = ['-date']