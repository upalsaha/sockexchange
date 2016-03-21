from django import forms

class SignUpForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	password = forms.CharField(label='Password', max_length=255)

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	password = forms.CharField(label='Password', max_length=255)

class CreateForm(forms.Form):
	name = forms.CharField(label='Name', max_length=30)
	material = forms.CharField(max_length=30)
	color = forms.CharField(max_length=30)
	description = forms.CharField(max_length=255)
	style = forms.CharField(max_length=30)
	theme = forms.CharField(max_length=30)
	price = forms.DecimalField(max_digits=3, decimal_places=2)