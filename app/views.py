from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':50,'b':20,'c':40}
    return render(request,'conditions.html',d)
def nested (request):
    d={'a':50,'b':200,'c':400}
    return render(request,'statement.html',d)
def loop(request):
    d={'name':'HARITHA'}
    return render(request,'loops.html',d)
