from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def home(request):
    return HttpResponse("<h1> Project is on AIR LIVE </h1>")

from myapp import forms

def builtinforms(request):

    form=forms.SampleForm()
    return render(request,"builtinform.html",{'form':form})

#forms is a file or a library 
#in forms Form is a class so we inherit from forms.Form