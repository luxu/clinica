from django import forms
from django.contrib.auth.models import User

from .models import Medico, Patient


class HospitalForm(forms.ModelForm):
	class Meta:
		model = Hospital
		fields = '__all__'

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(
		label='Senha',
		widget=forms.PasswordInput
	)
	password2 = forms.CharField(
		label='Repetir a senha',
		widget=forms.PasswordInput
	)

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'email'
		)

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError(
				'Senhas não coincidem'
			)
		return cd['password2']


class MedicoForm(forms.ModelForm):
	class Meta:
		model = Medico
		fields = [
			'user',
		]


class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = [
			'name',
			'medico',
			'is_atendimento'
		]