from django.urls import path

from . import views

appname = 'hospital'


urlpatterns = [
	path('', views.IndexListView.as_view(), name='index_list_view'),
	path('cadastrar_usuario', views.cadastrarUsuario, name="cadastrar_usuario"),
	path('pegar-hospital/', views.PegarHospital, name='pegar_hospital'),
	path('patients/', views.PatientsListView.as_view(), name='patient_list_view'),
	path('patients/create/', views.PatientsCreateView.as_view(), name='patient_create_view'),
	path('medicos/', views.MedicosListView.as_view(), name='medico_list_view'),
	path('medicos/create/', views.MedicosCreateView.as_view(), name='medico_create_view'),
	path('hospital/', views.HospitalListView.as_view(), name='hospital_list_view'),
]
