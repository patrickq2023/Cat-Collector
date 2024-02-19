from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat
from .forms import FeedingForm

# cats = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

# Create your views here.
# Include an .html file extension - unlike when rendering EJS templates

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cats_index(request):
  cats = Cat.objects.all()
   
  return render(request, 'cats/index.html', {
    'cats': cats
  })

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
   # instantiate FeedingForm to be rendered in the template 
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {
    'cat': cat,
    'feeding_form': feeding_form
    })

def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)

    if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
      new_feeding = form.save(commit=False)
      new_feeding.cat_id = cat_id
      new_feeding.save()
    return redirect('detail', cat_id=cat_id)

class CatCreate(CreateView):
  model = Cat
  fields = '__all__'

class CatUpdate(UpdateView):
  model = Cat
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'