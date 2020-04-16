from django.shortcuts import render
from App.forms import UserForm

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def register(request):
    user=UserForm()

    if request.method=="POST":
        user_input=UserForm(request.POST)


        user_input.save(commit=True)
        


    else:
        return render(request,'register.html',{'user':user})
