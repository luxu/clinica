from django.contrib import admin

from hospital.models import HospitalBase, Patient, Medico

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
	list_display = ['user']

@admin.register(HospitalBase)
class HospitalBaseAdmin(admin.ModelAdmin):
	save_on_top = True
	# list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login')
	list_display = [
		'id',
		'name',
	]
	filter_horizontal = ('medico',)
	# inlines = [MedicoAdmin]

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'medico',
		'is_atendimento',
	]


