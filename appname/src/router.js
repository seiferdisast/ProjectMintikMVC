import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';

// import actualizar from './components/actualizar.vue'
// import consultar from './components/consultar.vue'
// import registrar from './components/registrar'
import actualizarDatosPersonalesFamiliar from './components/actualizarDatosPersonalesFamiliar.vue'
import actualizarDatosPersonalesPaciente from './components/actualizarDatosPersonalesPaciente.vue'
import actualizarEnfermeroAsignado from './components/actualizarEnfermeroAsignado.vue'
import actualizarMedicoAsignado from './components/actualizarMedicoAsignado.vue'
import consultarPacientes from './components/consultarPacientes.vue';
import consultarDatosPaciente from './components/consultarDatosPaciente.vue'
import registrarEnfermero from './components/registrarEnfermero.vue'
import registrarFamiliar from './components/registrarFamiliar.vue'
import registrarMedico from './components/registrarMedico.vue'
import registrarPaciente from './components/registrarPaciente.vue'

const routes = [
  {
    path: '/',
    name: 'main',
    component: App
  },
  /*{
    path: '/update',
    name: "actualizar",
    component: actualizar,
  },*/
  {
    path: '/update/updateinforelative',
    name: "actualizardatosfamiliar",
    component: actualizarDatosPersonalesFamiliar,
  },
  {
    path: '/update/updateinfopatient',
    name: "actualizardatospaciente",
    component: actualizarDatosPersonalesPaciente,
  },
  {
    path: '/update/updateassignednurse',
    name: "actualizarenfermeroasignado",
    component: actualizarEnfermeroAsignado,
  },
  {
    path: '/update/updateassigneddoctor',
    name: "actualizarmedicoasignado",
    component: actualizarMedicoAsignado,
  },
  /*{
    path: '/read',
    name: "consultar",
    component: consultar,
  },*/
  {
    path: '/read/readpatients',
    name: "consultarpacientes",
    component: consultarPacientes,
  },
  {
    path: '/read/readpatientdata',
    name: "consultardatospacientes",
    component: consultarDatosPaciente,
  },
  /*{
    path: '/create',
    name: "registrar",
    component: registrar,
  },*/
  {
    path: '/create/createnurse',
    name: "registrarenfermero",
    component: registrarEnfermero,
  },
  {
    path: '/create/createrelative',
    name: "registrarfamiliar",
    component: registrarFamiliar,
  },
  {
    path: '/create/createdoctor',
    name: "registrarmedico",
    component: registrarMedico,
  },
  {
    path: '/create/createpatient',
    name: "registrarpaciente",
    component: registrarPaciente,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
