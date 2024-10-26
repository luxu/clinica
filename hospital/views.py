from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .forms import MedicoForm, PatientForm, UserRegistrationForm
from .models import HospitalBase, Medico, Patient


def cadastrarUsuario(request):
    if request.method == "POST":
        form_usuario = UserRegistrationForm(request.POST)
        if form_usuario.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form_usuario.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                form_usuario.cleaned_data['password']
            )
            # Save the User object
        form_usuario.save()
        # return redirect('index')
        return render(
            request,
            'registration/register_done.html',
            {'new_user': new_user}
        )
    else:
        form_usuario = UserRegistrationForm()
    return render(request, 'registration/cadastro.html', {'form_usuario': form_usuario})


class IndexListView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    paginate_by = 25

    def get_queryset(self):
        pk = self.request.user.id
        queryset = HospitalBase.objects.filter(medico__user_id=pk)
        return queryset


@login_required
def PegarHospital(request):
    template_name = 'hospital/hospitais_do_medico.html'
    id_do_hospital_do_medico = request.POST['id_hospital']
    hospital = HospitalBase.objects.get(id=id_do_hospital_do_medico)
    medicos = Medico.objects.filter(medicos_do_hospital__id=id_do_hospital_do_medico)
    contexto = {
        'hospital': hospital,
        'medicos': medicos
    }
    return render(request, template_name=template_name, context=contexto)


class HospitalListView(ListView):
    model = HospitalBase
    template_name = 'hospital/hospital_list.html'

class HospitalCreateView(FormView):
    # template_name = 'hospital/_form.html'
    form_class = HospitalForm
    success_url = reverse_lazy('hospital_list_view')


class PatientsListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'hospital/patient_list.html'
    queryset = Patient.objects.all()


class MedicosListView(LoginRequiredMixin, ListView):
    model = Medico
    template_name = 'hospital/medico_list.html'
    queryset = Medico.objects.all()


class MedicosCreateView(FormView):
    template_name = 'hospital/medico_form.html'
    form_class = MedicoForm
    success_url = reverse_lazy('medico_list_view')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PatientsCreateView(FormView):
    template_name = 'hospital/patient_form.html'
    form_class = PatientForm
    success_url = reverse_lazy('patient_list_view')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
