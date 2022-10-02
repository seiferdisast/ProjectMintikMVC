<template>
  <div id="app" class="app">
    <div class="header">
      <h1>Hospitalization At Home</h1>
      <nav>
        <button class="boton-nav-funciones" click="actualizar">
          <router-view v-on:click="actualizar"> Actualizar </router-view>
        </button>
      </nav>
      <nav>
        <button class="boton-nav-funciones" click="consultar">
          <router-view v-on:click="consultar"> Consultar </router-view>
        </button>
      </nav>
      <nav>
        <button class="boton-nav-funciones" click="registrar">
          <router-view v-on:click="registrar"> Registrar </router-view>
        </button>
      </nav>
    </div>

    <div class="main-component">
      <router-view v-on:registrar="registrar">
      </router-view>
    </div>
    
    <div class="footer">
      <h2>MisiónTIC 2022 - Equipo 1 Ciclo 3</h2>
    </div>
  </div>
</template>

<script>
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

export default {
  name: "App",
  data: function () {
    return {};
  },
  components: {},

  methods: {
    actualizar: function () {
      $router.push({ name: "actualizar" });
    }, 
    
    consultar: function () {
      $router.push({ name: "consultar" });
    },
    

    registrar: function () {
      this.$router.push({ name: "registrar" });
    },
    

    registrarPacientes: function () {
      this.$router.push({ name: "registrarPacientes" });
    },

    registrardoctor: function () {
      this.$router.push({ name: "registrardoctor" });
    },

    registrarpariente: function () {
      this.$router.push({ name: "registrarpariente" });
    },

    registrarenfermero: function () {
      this.$router.push({ name: "registrarenfermero" });
    },

    created: function () { },
  },

};
</script>

<style>
body {
  margin: 0 0 0 0;
}

.header {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;

  background-color: #1673b1;
  color: #e5e7e9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h1 {
  width: 20%;
  text-align: center;
}
.boton-nav-funciones {
    background-color: cadetblue;
    border: none;
    color: black;
    font-size: 1.50em;
    margin: 20px;
    padding: 10px;
    text-align: center;
    width: 300px;
    text-decoration: none;
    border-radius: 5px;
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif
}
</style>
