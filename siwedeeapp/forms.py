from django import forms

class LoginUsers(forms.Form):
	"""Class for login of students, teachers..."""
	username = forms.CharField(label='Contrasena')
	password = forms.CharField(widget=forms.PasswordInput, min_length=8, label='Usuario')

class AsesorLaboral(forms.Form):
	choices_calificacion = (
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
		(6, '6'),
		(7, '7'),
		(8, '8'),
		(9, '9'),
		(10, '10'),
		)

	responsabilidad = forms.ChoiceField(choices=choices_calificacion, label='Responsabilidad', required=False)
	trabajoEquipo = forms.ChoiceField(choices=choices_calificacion, label='Trabajo en Equipo', required=False)
	asistenciaPuntualidad =  forms.ChoiceField(choices=choices_calificacion, label='Asistencia y Puntualidad ', required=False)
	habilidadProblemas = forms.ChoiceField(choices=choices_calificacion, label='Habilidad ante Problemas', required=False)
	manejoHerramientas = forms.ChoiceField(choices=choices_calificacion, label='Manejo de Herramientas', required=False)
	disponibilidad = forms.ChoiceField(choices=choices_calificacion, label='Disponibilidad', required=False)
	respeto = forms.ChoiceField(choices=choices_calificacion, label='Respeto', required=False)
	imagenPersonal = forms.ChoiceField(choices=choices_calificacion, label='Imagen Personal', required=False)