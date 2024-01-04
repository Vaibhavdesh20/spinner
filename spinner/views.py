from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def member(request):
     return render(request,'member.html')

def prashant(request):
     return render(request,'prashant.html')

def member2(request):
     return render(request,'member2.html')

def history(request):
     return render(request,'history.html')

def member3(request):
     return render(request,'member3.html')

def services(request):
     return render(request,'services.html')