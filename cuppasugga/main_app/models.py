from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# MEALS = (
#     ('B', 'Breakfast'),
#     ('L', 'Lunch'),
#     ('D', 'Dinner')
# )

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    # If True, the field is allowed to be blank. Default is False

class Bag(models.Model):
    item = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    quantity = models.PositiveSmallIntegerField()
    # bag = models.ForeignKey(Bag, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

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