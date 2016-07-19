from django.shortcuts import render
from django.http import HttpResponseRedirect
from siwedeeapp.forms import LoginUsers
# Create your views here.

def login(request):
	if request.method=='POST':
		form = LoginUsers(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('siwedeeapp/sesion/')	#retorna a una vista
	else:
		form = LoginUsers()
	return render(request,'login.html',{'form': form})