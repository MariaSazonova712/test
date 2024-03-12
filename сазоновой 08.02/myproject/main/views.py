from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.views.generic import DeleteView, UpdateView
from .filters import PostFilter

def index(request):
    tasks_all = Product.objects.order_by('id')
    tasks = PostFilter(request.GET, queryset=tasks_all)
    print("***", tasks)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'tasks': tasks})



def delivery(request):
    return render(request, 'main/delivery.html')

def care(request):
    return render(request, 'main/care.html')

def add(request):
    error = ""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = ProductForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/add.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'
    template_name = 'main/task-delete.html'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'main/create.html'
    form_class=ProductForm
    success_url = '/'


