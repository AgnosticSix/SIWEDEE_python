from django.shortcuts import render
from django.http import HttpResponseRedirect
from siwedeeapp.forms import LoginUsers
from siwedeeapp.models import USUARIOS
# Create your views here.

def login(request):
	if request.method=='POST':
		form = LoginUsers(request.POST)
		if form.is_valid():
			try:
				username = request.POST['username']
				password = request.POST['password']
				valid = USUARIOS.objects.filter(USUARIO=username)
				if password in valid  :
					return HttpResponseRedirect('siwedeeapp/sesion')	#retorna a una vista, no programada
			except ValueError as e:
				print( e )
	else:
		form = LoginUsers()
	return render(request,'login.html',{'form': form})