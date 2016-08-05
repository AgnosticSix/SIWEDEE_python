from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from siwedeeapp.forms import LoginUsers
from siwedeeapp.models import CATPERSONAS, TIPOPERSONA
# Create your views here.

def loginUser(request):
	if request.method=='POST':
		form = LoginUsers(request.POST)
		if form.is_valid():
			try:
				userName = request.POST['username']
				userPassword = request.POST['password']
				accessUser = authenticate(username=userName, password=userPassword)
				if accessUser is not None and accessUser.is_active:
					login(request, user=accessUser)
					queryUser = CATPERSONAS.objects.filter(USUARIO=userName, PASSWORD=userPassword)
					tipoPersona = queryUser[0].IDTIPOPERSONA.NOMBRE
					return HttpResponseRedirect('sesion')	#retorna a una vista, no programada
			except Exception:
				print( 'Exception capturada' )
	else:
		form = LoginUsers()
	return render(request,'login.html',{'form': form})
