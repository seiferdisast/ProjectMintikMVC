<template>
    <section class="registros">
        <a href="Registrar.html" class="registros">
            <button v-on:click="" class="botonPrueba">Registrar</button>
        </a>
    </section>
</template>
  
<script>
export default {
    name: "App",

    data: function () { },

    methods: {},

    created: function () { },
};
</script>
  
<style>
.registros{
    width: 100%;
    height: 100px;
}
.botonesRegistros{
    width: 220px;
    height: 310px;
    display: flex;
    justify-content: space-between;
}
.botonPrueba{
    background: none;
    border-color: #33A8E0;
	color: black;
	font-size:1.25em;
	margin:25px;
	padding:15px;
	text-align:center;
	width:300px;
	text-decoration:none;
    box-shadow:0px 3px 0px #373c3c;
}
.botonPrueba:hover{
    box-shadow:0px 0px 0px;
    padding-top:7px;
}
</style>