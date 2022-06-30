from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from viewbooks.models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render


class UzBooksView(ListView):
    model = UzbBooksModel
    template_name = 'uzb.html'
    context_object_name = 'uzb_list'

class RusBooksView(ListView):
    model = RusBooksModel
    template_name = 'rus.html'
    context_object_name = 'rus_list'

class EngBooksView(ListView):
    model = EngBooksModel
    template_name = 'eng.html'
    context_object_name = 'eng_list'

class UzBooksDetailView(DetailView):
    model = UzbBooksModel
    template_name = 'uzdetail.html'
    context_object_name = 'uzb'

class RusBooksDetailView(DetailView):
    model = RusBooksModel
    template_name = 'rusdetail.html'
    context_object_name = 'rus'

class EngBooksDetailView(DetailView):
    model = EngBooksModel
    template_name = 'engdetail.html'
    context_object_name = 'eng'

class Onas(TemplateView):
    template_name ="onas.html" 

###
def uzbbuy(request, pk):
    context = {}
    book = get_object_or_404(UzbBooksModel, pk=pk )
    context['uzb'] = book
    if request.method == 'POST':
        form = UzBuyerForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.kitob = book
            print(form)
            form.save()

            return HttpResponseRedirect('/')
    else:
            form = UzBuyerForm()
    context['form'] = form
    return render(request, 'uzdetail.html', context)



def rusbuy(request, pk):
    context = {}
    book = get_object_or_404(RusBooksModel, pk=pk)
    context['rus'] = book
    if request.method == 'POST':
        form = RusBuyerForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.kitob = book
            print(form)
            form.save()

            return HttpResponseRedirect('/')
    else:
            form = RusBuyerForm()
    context['form'] = form
    return render(request, 'rusdetail.html', context)


def engbuy(request, pk):
    context = {}
    book = get_object_or_404(EngBooksModel, pk=pk)
    context['eng'] = book
    if request.method == 'POST':
        form = EngBuyerForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.kitob = book
            print(form)
            form.save()

            return HttpResponseRedirect('/')
    else:
            form = EngBuyerForm()
    context['form'] = form
    return render(request, 'engdetail.html', context)


class SerachUz(ListView):
    template_name = "search.html"
    def get_queryset(self):
        return UzbBooksModel.objects.filter(barcode = self.request.GET.get("q"))

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context 
