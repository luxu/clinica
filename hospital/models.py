from django.contrib.auth import get_user_model
from django.db import models

from .constants import TIPO_PESSOA


class HospitalBase(models.Model):
	name = models.CharField(max_length=50)
	medico = models.ManyToManyField('Medico', related_name='medicos_do_hospital')

	def __repr__(self):
		return f'Médico.: {self.medico} do Hospital.:{self.name}'

	def __str__(self):
		return self.name


class Patient(models.Model):
	medico = models.ForeignKey(
		'Medico',
		on_delete=models.CASCADE,
		null=True, blank=True
	)
	name = models.CharField(
		max_length=50,
	)
	is_atendimento = models.BooleanField(
		default=False
	)

	def __str__(self):
		return self.name


class Medico(models.Model):
	user = models.ForeignKey(
		'Person',
		on_delete=models.CASCADE,
		null=True
	)

	def __repr__(self):
		return f'Médico.: {self.name}'

	def __str__(self):
		return self.name


class Person(models.Model):
	user = models.OneToOneField(
		get_user_model(),
		on_delete=models.CASCADE,
		null=True
	)
	tipo_pessoa = models.CharField(
		max_length=1,
		choices=TIPO_PESSOA,
	)
	cpf = models.CharField(
		max_length=11,
		null=True, blank=True
	)

	def __str__(self):
		return self.user.name

	class Meta:
		verbose_name = 'Pessoa'
		verbose_name_plural = 'Pessoas'
		# ordering = 'id'
