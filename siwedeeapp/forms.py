from django import forms

class LoginUsers(forms.Form):
	"""Class for login of students, teachers..."""
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)