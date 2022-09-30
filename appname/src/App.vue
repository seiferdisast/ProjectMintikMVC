<template>
  <div id="app" class="app">
    <div class="header">
      <h1>Hospitalization At Home</h1>
      <nav>
        <button v-on:click="verDatosPaciente">Consultar Datos Paciente</button>
      </nav>
    </div>
    <div>
      <router-view>
      </router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",

  data: function () {},

  methods: {
    verDatosPaciente:function(){
      this.$router.push({name: "consultardatosPaciente"})
    }
  },

  created: function () {},
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
