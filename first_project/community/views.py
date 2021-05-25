from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Human
from .forms import NewHumanForm

# Create your views here.
def index(request):
    return render(request,'community/index.html')

def signup(request):

    form = NewHumanForm()

    if request.method == 'POST':
        form = NewHumanForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Form invalid")

    return render(request,'community/signup.html',{'form':form})
