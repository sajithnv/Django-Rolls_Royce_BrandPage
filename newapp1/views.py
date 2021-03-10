from django.shortcuts import render,redirect,get_object_or_404
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

def todoedit(request,pk):
    todoinstance=get_object_or_404(Todo,pk=pk)
    t1=TodoForm(request.POST or None,instance=todoinstance)
    if t1.is_valid():
        t1.save()
        return redirect('view')
    return render(request,'todoadd.html',{'form': t1})
def newedit(request):
    content=Todo.objects.all()
    return render(request,'edit.html',{'data':content})
def delete(request):
    content=Todo.objects.all()
    return render(request,'delete.html',{'data':content})
def tododelete(request,pk):
    todoinstance=get_object_or_404(Todo,pk=pk)
    if request.method=='POST':
        todoinstance.delete()
        return redirect('view')
    return render(request,'tododelete.html',{'form': todoinstance})
def gallery(request):
    return render(request,'gallery.html')
