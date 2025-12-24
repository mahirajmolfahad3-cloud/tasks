from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

class Form(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    if request.method == "POST":
        task = Form(request.POST)
        if task.is_valid():
            x = task.cleaned_data["task"]
            request.session["tasks"] += [x]
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, "tasks/add.html", {
                "form": task
            })
    return render(request, "tasks/add.html", {
        "form": Form()
    })