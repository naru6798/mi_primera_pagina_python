from django.shortcuts import redirect, render

from . import models, forms

def index(request):
    return render(request, 'producto/index.html')


# CATEGORIA - LISTVIEW

def categoria_list(request):
    categorias = models.Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request, 'producto/categoria_list.html', context)

# CATEGORIA - CREATEVIEW

def categoria_form(request):
    if request.method == "GET":
        form = forms.CategoriaForm()
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:categoria_list")
    return render(request, "producto/categoria_form.html", {"form": form})

# CATEGORIA - UPDATEVIEW

def categoria_update(request, pk:int):
    query = models.Categoria.objects.get(id=pk)
    if request.method == "GET":
        form = forms.CategoriaForm(instance=query)
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            
            return redirect("producto:categoria_list")
        
    return render(request, "producto/categoria_form.html", {"form": form})


# CATEGORIA - DELETEVIEW

def categoria_delete(request, pk:int):
    query = models.Categoria.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("producto:categoria_list")
    return render(request, "producto/categoria_confirm_delete.html", {"object": query})