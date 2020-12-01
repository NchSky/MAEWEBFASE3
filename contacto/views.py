from django.shortcuts import render, redirect , get_object_or_404
from . models import Entrada, Formulario
from django.views import generic
from . forms import EntradaForm, FormularioForm

# Create your views here.
def index(request):
    #num_entrada = Entrada.objects.all().count()

    return render(
        request,
        'index.html',
        #context={'numero_entradas': num_entrada},
    )

def ayuda(request):
    
    return render(
        request,
        'necesitoayuda.html',
    )

def amistadestoxicas(request):
    
    return render(
        request,
        'necesitoayuda2.html',
    )

def diferencias(request):
    
    return render(
        request,
        'necesitoayuda3.html',
    )

def suicidio(request):
    
    return render(
        request,
        'necesitoayuda4.html',
    )

def acososexual(request):
    
    return render(
        request,
        'necesitoayuda5.html',
    )

def redesSociales(request):
    
    return render(
        request,
        'necesitoayuda6.html',
    )

def paginasAyuda(request):
    
    return render(
        request,
        'necesitoayuda7.html',
    )              



from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic

class EntradaCreate(CreateView):
    model = Entrada
    fields = '__all__'

class EntradaUpdate(UpdateView):
    model = Entrada
    fields = ['titulo', 'tema']

class EntradaDelete(DeleteView):
    model = Entrada
    success_url = reverse_lazy('index')


class EntradaDetailView(generic.DetailView):
    model = Entrada

class EntradaListView(generic.ListView):
    model = Entrada
    template_name = 'templates/contacto/entrada_list.html'
    queryset = Entrada.objects.all()
    paginate_by = 10

def entrada_new(request):
    if request.method == "POST":
        form = EntradaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('entrada-detail', pk=post.pk)
    else:
        form = EntradaForm()
        return render(request, 'contacto/entrada_form.html', {'form': form})

def entrada_edit(request, pk):
    post = get_object_or_404(Entrada, pk=pk)
    if request.method == "POST":
        form = EntradaForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('entrada-detail', pk=post.pk)
    else:
        form = EntradaForm(instance=post)
    return render(request, 'contacto/entrada_form.html', {'form': form})


class FormularioCreate(CreateView):
    model = Formulario
    fields = '__all__'

class FormularioUpdate(UpdateView):
    model = Formulario
    fields = ['detalle']

class FormularioDelete(DeleteView):
    model = Formulario
    success_url = reverse_lazy('index')


class FormularioDetailView(generic.DetailView):
    model = Formulario


class FormularioListView(generic.ListView):
    model = Formulario
    template_name = 'templates/contacto/formulario_list.html'
    queryset = Formulario.objects.all()
    paginate_by = 10

def formulario_new(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('formulario-detail', pk=post.pk)
    else:
        form = FormularioForm()
        return render(request, 'contacto/formulario_form.html', {'form': form})

def formulario_edit(request, pk):
    post = get_object_or_404(Formulario, pk=pk)
    if request.method == "POST":
        form = FormularioForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('formulario-detail', pk=post.pk)
    else:
        form = FormularioForm(instance=post)
    return render(request, 'contacto/formulario_form.html', {'form': form})