import {Routes} from '@angular/router'
import {HomeComponent} from './home/home.component'
// import {PacienteComponent} from './paciente/paciente.component'
// import {FisioterapeutaComponent} from './fisioterapeuta/fisioterapeuta.component'
// import {ConsultasComponent} from './consultas/consultas.component'
import {AgendarComponent} from './agendar/agendar.component'

export const ROUTES: Routes = [
  {path: '', component: HomeComponent},
  // {path: 'paciente', component: PacienteComponent},
  // {path: 'fisioterapeuta', component: FisioterapeutaComponent},
  // {path: 'consultas', component: ConsultasComponent},
  {path: 'agendar', component: AgendarComponent},
]
