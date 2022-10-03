<template>
  <div id="app" class="app">
    <div class="header">
      <img class="iconHome" src="http://drive.google.com/uc?export=view&id=1PMxF5Yn-dWEIstfQjE2eerCK0hmRWrjX">
      <a href="/"><img class="userIcon" src="http://drive.google.com/uc?export=view&id=1EtZyPK7ybz4Kz2bybnwy9l0QbeHbgw-v"></a>
    </div>
    <div class="menu">
    <nav class="barra">
      <ul class="nav">
        <li><a href="">REGISTRAR</a>
          <ul>
            <li><a href="/create/createpatient">Registrar paciente</a></li>
            <li><a href="/create/createdoctor">Registrar médico</a></li>
            <li><a href="/create/createnurse">Registrar enfermero</a></li>
            <li><a href="/create/createrelative">Registrar familiar</a></li>
          </ul>
        </li>
        <li><a href="">ACTUALIZAR</a>
          <ul>
            <li><a href="/update/updateinfopatient">Actualizar paciente</a></li>
            <li><a href="/update/updateassigneddoctor">Actualizar médico</a></li>
            <li><a href="/update/updateassignednurse">Actualizar enfermero</a></li>
            <li><a href="/update/updateinforelative">Actualizar familiar</a></li>
          </ul>
        </li>
        <li><a href="">CONSULTAR</a>
          <ul>
            <li><a href="/read/readpatients">Consultar pacientes</a></li>
            <li><a href="/read/readpatientdata">Consultar datos paciente</a></li>
          </ul>
        </li>
      </ul>
    </nav><!-- Aqui estamos cerrando la nueva etiqueta nav -->
  </div>
  <router-view v-on:registrar="registrar">
  </router-view>
    <div class="footer">
      <div class="foteer__main_container">
        <div class="container">
            <div class="type__icon">
                <img class="icon" src="http://drive.google.com/uc?export=view&id=1ZSBEJvx82aO-nP61uiOnSxB86skvBCPf">
            </div>
            <div class="type__content">
                <h5>Nuestas oficinas</h5>
                <p>Calle 43 # 12-15 <br> Transversal 94 # 45-12</p>
            </div>
        </div>
        <div class="container">
            <div class="type__icon">
                <img class="icon" src="http://drive.google.com/uc?export=view&id=1wYW_VjNtosmw44cJorkXktUQO1fhHeda">
            </div>
            <div class="type__content">
                <h5>Líneas de atención</h5>
                <p>01 8000 66 66 66 <br> Bogotá +57 654 878 2565</p>
            </div>
        </div>
        <div class="container">
            <div class="type__icon">
                <img class="icon" src="http://drive.google.com/uc?export=view&id=1X39YGWVo7732NM6mvgILzOxWlLq1ONSq">
            </div>
            <div class="type__content">
                <h5>Línea Covid-19/ Viruela Símica</h5>
                <p>01 8000 11 22 33 <br> Bogotá +57 456 878 2565</p>
            </div>
        </div>
    </div>
    <div class="footer__links">
        <p>2022 © Todos los derechos reservados ǀ Términos y condiciones ǀ Políticas de privacidad ǀ Lineamientos de
            seguridad ǀ Sostenibilidad</p>
    </div>
    <div class="footer__recomendations">
        <p>Navegadores recomendados: Internet Explorer 10.0 o superior; Google Chrome, Firefox o Safari en su última
            versión</p>
    </div>
    <div class="developers">
        <div class="developers__icon">
            <img class="icon" src="http://drive.google.com/uc?export=view&id=1rfZQmNBI7DbJjMTFp0SjyPu92RE-qBQe">
        </div>
        <div class="developers__members">
            <p>Developed by
            <h5><a href="https://github.com/Darly145">Darly Rodríguez</a> - <a
                    href="https://github.com/VampDanny">Daniel Sánchez</a> - <a
                    href="https://github.com/dgguzmangr">David Guzmán</a> - <a
                    href="https://github.com/seiferdisast">Daniel Rodríguez</a> - <a
                    href="https://github.com/Muchiha91">David Chávez</a></h5>
            </p>
        </div>
    </div>
    <div class="socialnetworks">
        <div id="socialnetworks__icon">
            <img class="icon" src="http://drive.google.com/uc?export=view&id=1q5ghppEuBRk5uxpU3eeA7IatS9AO0_d6">
            <img class="icon" src="http://drive.google.com/uc?export=view&id=1UlisqL6wS3EsVvn7VfaWWTDdhrCwUwUz">
            <img class="icon" src="http://drive.google.com/uc?export=view&id=1V3988Ul6iko1pxYjYnF_otFwL5fc-hR1">
            <img class="icon" src="http://drive.google.com/uc?export=view&id=1dRz9jFgqA15wS1Kkbq7tvn4kWXNfMgQo">
            <img class="icon" src="http://drive.google.com/uc?export=view&id=1GutCECIOqujiyLSlzMirCPd_wvzsraGs">
        </div>
    </div>
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
  background-color: darkslategrey;
  width: 100%;
  height: 95px;
  display: flex;
}


.iconHome {
  width: 115px;
  height: 90px;
  margin-left: 5px;
}

.userIcon {
  width: 70px;
  height: 70px;
  margin-left: 1670px;
  margin-top: 10px;
}

.homeIcon {
  width: 50px;
  height: 50px;
}
.buttonHome {
  background-color: darkslategrey;
  width: 1500px;
  border: none;
}
.menu {
  margin: auto;
  width: 1000px;
  font-family: Arial, Helvetica, sans-serif;
}

ul,
ol {
  list-style: none;
}

.nav {
  width: 500px;
  margin: 0 auto;
}

.nav>li {
  float: left;
}

.nav li a {
  background-color:steelblue;
  color: #fff;
  text-decoration: none;
  padding: 20px 12px;
  display: block;
}

.nav li a:hover {
  background-color: #434343;
}

.nav li ul {
  display: none;
  position: absolute;
  min-width: 140px;
}

.nav li:hover>ul {
  display: block;
}

.nav li ul li {
  position: relative;
}

.nav li ul li ul {
  right: -140px;
  top: 0px;
}
.barra{
  width: auto;
  height: 58px;
}
.footer {
    padding-bottom: 5rem;
    margin-top: 4rem;
    width: min(100%, 120rem);
    margin: auto;
    background-color: gray
}

.foteer__main_container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    text-align: center;
    background-color: #ffffff;
}

.type__icon {
    height: 1.5rem;
}

.type__content {
    font-family: var(--fuenteParrafos);
    font-size: 0.8rem;
    line-height: 2;
}

.footer__links {
    font-family: var(--fuenteParrafos);
    font-size: 0.8rem;
    line-height: 2;
    text-align: center;
}

.footer__recomendations {
    font-family: var(--fuenteParrafos);
    font-size: 0.9rem;
    line-height: 2;
    text-align: center;
}

.developers {
    font-family: var(--fuenteParrafos);
    font-size: 0.9rem;
    line-height: 2;
    text-align: center;
}

.developers__icon {
    height: 1.5rem;
}

.socialnetworks {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
}

#socialnetworks__icon {
    position: absolute;
    padding-left: 810px;
}
.icon {
    width: 40px; 
    max-height: 200%; 
    margin-left: 20px;
}

</style>



