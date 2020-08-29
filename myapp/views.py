from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def home(request):
    return HttpResponse("<h1> Project is on AIR LIVE </h1>")

from myapp import forms

def builtinforms(request):

    if request.method=="POST":
        
        # Creating a form instance with the data filled in all fields will get the specified value
        form=forms.SampleForm(request.POST)
        
        if form.is_valid():
        
            # cleaned_data is variable in form instance that holds the dictionary containing the data 
            # that we have filled 
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            phno=form.cleaned_data.get('phno')
            pwd=form.cleaned_data.get('pwd')
            birth_day=form.cleaned_data.get('birth_day')
            birth_month=form.cleaned_data.get('birth_month')
            birth_year=form.cleaned_data.get('birth_year')
            gender=form.cleaned_data.get('gender')
            data=form.cleaned_data
            return render(request,"displaydata.html",context=data)


    form=forms.SampleForm()
    return render(request,"builtinform.html",{'form':form})

#forms is a file or a library 
#in forms Form is a class so we inherit from forms.Form