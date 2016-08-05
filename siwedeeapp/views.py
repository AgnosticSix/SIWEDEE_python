from django.shortcuts import render
from django.http import HttpResponseRedirect
from siwedeeapp.forms import LoginUsers
from siwedeeapp.models import CATPERSONAS, TIPOPERSONA
# Create your views here.

def login(request):
	if request.method=='POST':
		form = LoginUsers(request.POST)
		if form.is_valid():
			try:
				username = request.POST['username']
				password = request.POST['password']
				queryUser = CATPERSONAS.objects.filter(USUARIO=username, PASSWORD=password)
				if queryUser:
					tipoPersona = queryUser[0].IDTIPOPERSONA.NOMBRE
					print('Funciona:',tipoPersona)
					return HttpResponseRedirect('sesion')	#retorna a una vista, no programada
			except Exception:
				print( 'Exception capturada' )
	else:
		form = LoginUsers()
	return render(request,'login.html',{'form': form})
