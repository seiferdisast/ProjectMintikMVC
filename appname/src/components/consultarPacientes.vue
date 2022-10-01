<template>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <div class="derecha_3">
    <div class="marco_3">
      <form class="forma_3" v-on:submit.prevent="agregarlista">
        <div class="boton_lateral_3">
          <div class="boton_consultar_pacientes_registrado">
            <button type="submit">Consultar</button>
          </div>
        </div>
      </form>
      <div class="consulta_registro">
        <table>
          <tr>
            <th><strong>Cedula</strong></th>
            <th><strong>nombre</strong></th>
            <th><strong>apellido</strong></th>
            <th><strong>celular</strong></th>
            <th><strong>direccion</strong></th>
            <th><strong>email</strong></th>
            <th><strong>rol</strong></th>
            <th><strong>doctor asignado</strong></th>
            <th><strong>enfermera asignado</strong></th>
            <th><strong>pariente</strong></th>
          </tr>

          <tr v-for="item in lista">
            <td v-text="item.documentId"></td>
            <td v-text="item.name"></td>
            <td v-text="item.lastname"></td>
            <td v-text="item.cellullarPhone"></td>
            <td v-text="item.address"></td>
            <td v-text="item.email"></td>
            <td v-text="item.role"></td>
            <td v-text="item.assignDoctor"></td>
            <td v-text="item.assignNurse"></td>
            <td v-text="item.assignRelative"></td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "consultarpacientes",
  data: function () {
    return {
      lista: [
        {
          documentId: "",
          name: "",
          lastname: "",
          cellullarPhone: "",
          address: "",
          email: "",
          role: "",
          assignDoctor: "",
          assignNurse: "",
          assignRelative: "",
        },
      ],
    };
  },

  methods: {
    agregarlista: function () {
      const url ="http://127.0.0.1:8000/users/?role=paciente";
      axios.get(url).then((result) => {
        this.lista = result.data;
      });
    },
    Link_Consultar_Paciente: function () {
      this.$router.push("/users/");
    },
  },
};
</script>

<style>
body {
  margin: 0 0 0 0;
  padding: 0;
}
.derecha_3 {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.marco_3 {
  border: 3px solid #283747;
  border-radius: 20px;
  width: 70%;
  height: 60%;
  background: white;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.marco_3 button {
  width: 800px;
  height: 30px;
  border: 1px solid #283747;
  color: #e5e7e9;
  border-radius: 3px;
  background: #2b63a0;
}
.marco_3 button:hover {
  border: 3px solid white;
  background: #2b63a0;
}
.consulta_registro {
  height: 70px;
  width: 810px;
  margin: 5px 5px;
}
.consulta_registro table {
  height: auto;
  width: 800px;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 15px;
  border: 1px solid black;
  border-spacing: 0;
}
.consulta_registro table td {
  border: 1px solid black;
}
.consulta_registro table th {
  border: 1px solid black;
}
</style>
