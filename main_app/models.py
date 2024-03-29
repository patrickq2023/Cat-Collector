from django.contrib import admin
from django.db import models
from django.urls import reverse
from datetime import date


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def fed_for_today(self):
      return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)  

    # Changing this instance method, does not impact the DB
    #therefore no migration required

  def __str__(self):
    return f'{self.name} ({self.id})'
    
  def get_absolute_url(self):
      return reverse('detail', kwargs={'cat_id': self.id})
    
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date} eaten by {self.cat}"
  
  # change the default sort
  class Meta:
    ordering = ['-date']

