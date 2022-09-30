import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

import consultardatosPaciente from './components/consultardatosPaciente.vue'
import consultarPacientes from './components/consultarPacientes.vue'
import registrarFamiliar from './components/registrarFamiliar.vue'  

const routes = [{
 path: '/',
 name: 'root',
 component: App
},
{
path: '/pacientData',
name: 'consultardatosPaciente',
component: consultardatosPaciente
},
]
const router = createRouter({
 history: createWebHistory(),
 routes
})
export default router