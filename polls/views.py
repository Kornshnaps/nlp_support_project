from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import TaskPreds
from .SupportVectorM import Predictor
from django.template import loader
from django.http import JsonResponse
from .forms import NewPredictorData, UserForm
import json
#from rest_framework import generics
def index(request):
    #submitbutton = request.POST.get("submit")

    task1 = ''
    form = UserForm(request.POST or None)

    if form.is_valid():
       task1 = form.cleaned_data.get("task")
       p = TaskPreds(task = task1, predCat= Predictor().predict(task1),num=form.cleaned_data.get("num"), recruit='Вова')

       p.save()
       print(p.as_json())
    #context = {'form': form,  'task': task1}
    #p = TaskPreds
    #p.task = task
    #p.save()
    return render(request, 'polls/formass.html')#, context)

def getJsonPred(request):
    #submitbutton = request.POST.get("submit")
    if request.method == 'GET':
        print('get')
    elif request.method == 'POST':
        print('Post')
    task1 = ''
    form = UserForm(request.GET or None)

    if form.is_valid():
        task1 = form.cleaned_data.get("task")
        p = TaskPreds(task = task1, predCat= Predictor().predict(task1),num=form.cleaned_data.get("num"),recruit = 'Вова')

        p.save()
    #context = {'task': p.task,'date':p.date,'num':p.num,'predictionNum':p.predCat}
    #p = TaskPreds
    #p.task = task
    #p.save()
    return JsonResponse(p.as_json())


def vote(request):

    return render(request, 'polls/index.html')
import pickle
def handle_uploaded_file(f):

    with open('polls/datas/new_data.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def refit(request):
    if request.method == 'POST':
        form = NewPredictorData(request.POST, request.FILES)
        if form.is_valid():
            print('eeee')
            handle_uploaded_file(request.FILES['file'])
        #k = request.FILES['file']

        return render(request, 'polls/refit.html', {'form':form})
    else:
        form = NewPredictorData()
    return render(request, 'polls/refit.html', {'form': form})


def index22(request):

    latest_question_list = TaskPreds.objects.order_by('id')[:]
    #output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

