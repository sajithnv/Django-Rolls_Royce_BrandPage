from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from newapp1.models import Todo
from newapp1.forms import TodoForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
##
### Create your views here.
##from django.http import HttpResponse
def f2(request):
    return render(request,'home.html')

@login_required
def todoadd(request):
    t=TodoForm(request.POST or None)
    if t.is_valid():
        t.save()
        return redirect('newapp12:view')
    return render(request,'todoadd.html',{'form1': t})

# def view(request):
#     content=Todo.objects.all()
#     return render(request,'view.html',{'data':content})
 
class view(LoginRequiredMixin,ListView):
    model=Todo
    template_name='view.html'
    queryset=Todo.objects.all()
    context_object_name='data'
    def get_queryset(self):
        return self.queryset.filter()

def help1(request):
    return render(request,'help.html')
def contact1(request):
    return render(request,'contact.html')
def todoedit(request,pk):
    todoinstance=get_object_or_404(Todo,pk=pk)
    t1=TodoForm(request.POST or None,instance=todoinstance)
    if t1.is_valid():
        t1.save()
        return redirect('newapp12:view')
    return render(request,'todoadd.html',{'form1': t1})
@login_required    
def newedit(request):
    content=Todo.objects.all()
    return render(request,'edit.html',{'data':content})
@login_required
def delete(request):
    content=Todo.objects.all()
    return render(request,'delete.html',{'data':content})
def tododelete(request,pk):
    todoinstance=get_object_or_404(Todo,pk=pk)
    if request.method=='POST':
        todoinstance.delete()
        return redirect('newapp12:view')
    return render(request,'tododelete.html',{'form1': todoinstance})
def gallery(request):
    return render(request,'gallery.html')
