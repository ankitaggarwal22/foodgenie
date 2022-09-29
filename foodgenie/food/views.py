from django.shortcuts import render,redirect
from . import models
from . import forms

# Create your views here.
def index(request):
    item_list=models.Item.objects.all()
    context={
        'item_list':item_list,
    }
    return render(request, 'index.html', context)

def detail(request, item_id):
    item=models.Item.objects.get(id=item_id)
    context={
        'item':item,
    }
    return render(request, 'detail.html', context)

def add_item(request):
    form=forms.ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'add_item.html', {'form':form})

def edit_item(request, id):
    item = models.Item.objects.get(id=id)
    form = forms.ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'add_item.html', {'form':form, 'item':item})

def delete_item(request, id):
    item = models.Item.objects.get(id=id)

    if request.method=='POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'item_delete.html', {'item':item})

