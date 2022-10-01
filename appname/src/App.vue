<template>
  <div id="app" class="app">
    <div class="header">
      <h1>Hospitalization At Home</h1>
      <nav>
        <button class="boton-nav-funciones" click="consultarPacientes">
          Consultar Pacientes
        </button>
      </nav>
    </div>
    <div class="main-component">
      <router-view v-on:click="consultarPacientes"> </router-view>
    </div>

    <div class="footer">
      <h2>MisiónTIC 2022 - Equipo 1 Ciclo 3</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data: function () {
    return {};
  },
  components: {},

  methods: {
    consultarPacientes: function () {
      $router.push({ name: "consultarpacientes" });
    },
    created: function () {},
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

  background-color: #283747;
  color: #e5e7e9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h1 {
  width: 20%;
  text-align: center;
}
</style>
