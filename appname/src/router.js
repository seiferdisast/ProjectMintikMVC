import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';

import consultarPacientes from './components/consultarPacientes.vue';

const routes = [
  {
    path:'/',
    name: 'root',
    component: App
  },
  {
    path: '/users',
    name: "consultarpacientes",
    component: consultarPacientes,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
