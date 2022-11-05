<template>
    <div class="signupFrm">
      <form v-on:submit.prevent="actualizarPaciente" class="form">
        <h1 class="title">Actualizar Datos Personales Paciente</h1>
        <div class="inputContainer">
          <input type="text" class="input" v-model="user.documentId" placeholder="a" />
          <label for="" class="label">Documento</label>
        </div>
        <div class="inputContainer">
          <input type="text" v-model="user.name" class="input" placeholder="a" />
          <label for="" class="label">Nombre</label>
        </div>
        <div class="inputContainer">
          <input type="text" class="input" v-model="user.lastName" placeholder="a" />
          <label for="" class="label">Apellido</label>
        </div>
        <div class="inputContainer">
          <input type="text" class="input" v-model="user.cellularPhone" placeholder="a" />
          <label for="" class="label">Celular</label>
        </div>
        <div class="inputContainer">
          <input type="text" class="input" v-model="user.address" placeholder="a" />
          <label for="" class="label">Direccion</label>
        </div>
        <div class="inputContainer">
          <input type="text" class="input" v-model="user.email" placeholder="a" />
          <label for="" class="label">Email</label>
        </div>
        <div class="inputContainer">
          <input type="text" class="input" v-model="user.role" placeholder="a" />
          <label for="Paciente" class="label">Rol</label>
        </div>
        <div class="inputContainer">
          <input type="text" class="input" v-model="user.password" placeholder="a" />
          <label for="Paciente" class="label">Password</label>
        </div>
        <div class="inputContainer">
          <input type="text" class="input" v-model="user.doctor_asignado" placeholder="a" />
          <label for="" class="label">Doctor Asignado</label>
        </div>
        <div class="inputContainer">
          <input type="text" class="input" v-model="user.enfermero_asignado" placeholder="a" />
          <label for="" class="label">Enfermero Asignado</label>
        </div>
        <div class="inputContainer">
          <input type="text" class="input" v-model="user.familiar" placeholder="a" />
          <label for="" class="label">Familiar Asignado</label>
        </div>
        <button type="submit">ACTUALIZAR</button>
        </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    name: 'registrarPacientes',
  
    data: function () {
      return {
        user: {
          documentId: "5555",
          name: "",
          lastName: "",
          cellularPhone: "",
          address: "",
          email: "",
          role: "Paciente",
          password: "",
          doctor_asignado: "",
          enfermero_asignado: "",
          familiar: "",
        },
      };
    },
  
    methods: {
      actualizarPaciente (){
        let post = {
          "documentId": this.user.documentId,
          "name": this.user.name,
          "lastName": this.user.lastName,
          "cellularPhone": this.user.cellularPhone,
          "address": this.user.address,
          "email": this.user.email,
          "role": this.user.role,
          "password": this.user.password,
          "doctor_asignado": this.user.doctor_asignado,
          "enfermero_asignado": this.user.enfermero_asignado,
          "familiar": this.user.familiar,
        }
        axios.patch("http://127.0.0.1:8000/user/5555/update/", post).then(result =>{
          this.user.documentId = "";
          this.user.name = "";
          this.user.lastName = "";
          this.user.cellularPhone= "";
          this.user.address = "";
          this.user.email = "";
          this.user.role = "";
          this.user.password = "";
          this.user.doctor_asignado = "";
          this.user.enfermero_asignado = "";
          this.user.familiar = "";
        })
      }
  
    },
    created: function () {
    }
  }
  </script>
  
  <style>
  .signupFrm {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  .form {
    background-color: beige;
    width: 900px;
    border-radius: 8px;
    padding: 20px 40px;
    box-shadow: 0 10px 25px rgba(92, 99, 105, 0.2);
  }
  .title {
    font-family: Georgia, "Times New Roman", Times, serif;
    font-size: 50px;
    margin-bottom: 50px;
  }
  .inputContainer {
    position: relative;
    height: 45px;
    width: 90%;
    margin-bottom: 17px;
  }
  .input {
    position: absolute;
    top: 0px;
    left: 0px;
    height: 100%;
    width: 100%;
    border: 1px solid gray;
    border-radius: 7px;
    font-size: 16px;
    padding: 0 20px;
    outline: none;
    background: none;
    z-index: 1;
  }
  
  ::placeholder {
    color: transparent;
  }
  .label {
    position: absolute;
    top: 15px;
    left: 15px;
    padding: 0 4px;
    color: black;
    background-color: beige;
    font-size: 16px;
    transition: 0.5s;
    z-index: 0;
  }
  
  .input+label {
    top: -7px;
    left: 3px;
    z-index: 10;
    font-size: 14px;
    font-weight: 600;
    color: purple;
  }
  .forma input{
      width: 100%;
  }
  </style>
