from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from datetime import datetime, timedelta
# Create your views here.
def todos(request):
    cur_day = datetime.today()
    todo_list = [{
            'title': "Task {}".format(i),
            'created': cur_day.strftime("%d/%m/%y"),
            'due_on': (cur_day + timedelta(days=3)).strftime("%d/%m/%y"),
            'owner': "admin",
            'mark': True
        }
        for i in range(1,5)
    ]
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'todo_list.html', context)
    

def completed_todos(request, index):
    cur_day = datetime.today()
    task = {
        'title': "Task {}".format(index),
        'created': cur_day.strftime("%d/%m/%y"),
        'due_on': (cur_day + timedelta(days=3)).strftime("%d/%m/%y"),
        'owner': "admin",
        'mark':False
    }
    context = {
        'task': task
    }
    return render(request, 'completed_todo_list.html', context)