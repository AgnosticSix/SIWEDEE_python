from django.shortcuts import render
from django.http import HttpResponseRedirect
from siwedeeapp.forms import LoginUsers
from siwedeeapp.models import CATPERSONAS
# Create your views here.

def login(request):
	if request.method=='POST':
		form = LoginUsers(request.POST)
		if form.is_valid():
			try:
				username = request.POST['username']
				password = request.POST['password']
				valid = CATPERSONAS.objects.filter(USUARIO=username)
				if len(valid)>0 and password==str(valid[0]):
					return HttpResponseRedirect('sesion')	#retorna a una vista, no programada
			except Exception:
				print( 'Exception capturada' )
	else:
		form = LoginUsers()
	return render(request,'login.html',{'form': form})