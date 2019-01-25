import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';

// import 'rxjs/add/operator/map';

// import { Dados } from './dados.model'
import { TiposAgendamentos } from './tipos-agendar.model'

@Component({
  selector: 'app-agendar',
  templateUrl: './agendar.component.html',
  styleUrls: ['./agendar.component.css']
})
export class AgendarComponent implements OnInit {

  tiposAgendamentos: TiposAgendamentos[] = [
    {nome:"Ortopedia"},
    {nome:"Neurológica"},
    {nome:"Outras"},
  ]

  usuario: any = {
    id: null,
    paciente: 'Luciano',
    fisioterapeuta: 'Dr. Perla',
    data: '21/01/2019',
    hora: '14:30',
    gravacao: new Date(),
    tipo: null
  }

  constructor(private http: Http) { }

  ngOnInit() {
  }

  onSubmit(form){
    // let url = 'https://httpbin.org/post'
    // this.http.post(url,JSON.stringify(form.value))
    // .map(res => res)
    // .subscribe(dados => console.log(dados));

  }

  verificaValidTouched(campo){
    return !campo.valid && campo.touched;
  }

  aplicaCssErro(campo) {
    return {
      'has-error': this.verificaValidTouched(campo),
      'has-feedback': this.verificaValidTouched(campo)
    }
  }

}
