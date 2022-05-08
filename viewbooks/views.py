from importlib.resources import contents
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from viewbooks.models import *
from .forms import *
#
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


###
def uzbbuy(request):

    if request.method == 'POST':

        form = BuyerForm(request.POST)

        if form.is_valid():
            # Сохранение формы
            form.save()

            # Редирект на ту же страницу
            return HttpResponseRedirect('uzb')
    else:
            form = BuyerForm()
            names = UzbBooksModel.objects.all()


    
    return render(request, 'uzbbuy.html', {'form': form, 'names':names})



def rusbuy(request):

    if request.method == 'POST':

        form = BuyerForm(request.POST)

        if form.is_valid():
            # Сохранение формы
            form.save()

            # Редирект на ту же страницу
            return HttpResponseRedirect('rus')
    else:
            form = BuyerForm()
            names = RusBooksModel.objects.all()

            

    
    return render(request, 'rusbuy.html', {'form': form, 'naames':names})

def engbuy(request):

    if request.method == 'POST':

        form = BuyerForm(request.POST)

        if form.is_valid():
            # Сохранение формы
            form.save()

            # Редирект на ту же страницу
            return HttpResponseRedirect('eng')
    else:
            
            form = BuyerForm()
            names = EngBooksModel.objects.all()

    
    return render(request, 'engbuy.html', {'form': form, 'names':names})