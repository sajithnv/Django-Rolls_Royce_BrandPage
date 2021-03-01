from django.shortcuts import render,redirect
from newapp1.models import Todo
from newapp1.forms import TodoForm
##
### Create your views here.
##from django.http import HttpResponse
def f2(request):
    return render(request,'home.html')
##def f2_1(request):
##    return render(request,'home.html')
def todoadd(request):
    t=TodoForm(request.POST or None)
    if t.is_valid():
        t.save()
        return redirect('view')
    return render(request,'todoadd.html',{'form': t})
def view(request):
    content=Todo.objects.all()
    return render(request,'view.html',{'data':content})
def help1(request):
    return render(request,'help.html')
def contact1(request):
    return render(request,'contact.html')
