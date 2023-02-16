from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
# Create your views here.
def sign_in(request):
	sign_up_form=UserCreationForm(request.POST or None)
	if sign_up_form.is_valid():
		sign_up_form.save()
		u=sign_up_form.cleaned_data.get('username')
		p=sign_up_form.cleaned_data.get('password1')
		user=authenticate(username=u,password=p)
		login(request, user)
		return redirect('home1')
	return render(request,'signin.html',{'form': sign_up_form})	