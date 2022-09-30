<template>
    <div class="signupFrm">
            <form action="" class="form">
              <h1 class="title">Consultar datos paciente</h1>
              <div class="inputContainer">
                <input type="text" class="input" placeholder="a">
                <label for="" class="label">DocumentId</label>
              </div>
        
              <div class="inputContainer">
                <input type="text" class="input" placeholder="a">
                <label for="" class="label">Name</label>
              </div>
        
              <div class="inputContainer">
                <input type="text" class="input" placeholder="a">
                <label for="" class="label">Last name</label>
              </div>
              <div class="inputContainer">
                <input type="text" class="input" placeholder="a">
                <label for="" class="label">Cell phone</label>
              </div>
              <div class="inputContainer">
                <input type="text" class="input" placeholder="a">
                <label for="" class="label">Adress</label>
              </div>
              <div class="inputContainer">
                <input type="text" class="input" placeholder="a">
                <label for="" class="label">Email</label>
              </div>
              <div class="inputContainer">
                <input type="text" class="input" placeholder="a">
                <label for="" class="label">Role</label>
              </div>
              <div class="inputContainer">
                <input type="text" class="input" placeholder="a">
                <label for="" class="label">Password</label>
              </div>
              <div class="inputContainer">
                <input type="text" class="input" placeholder="a">
                <label for="" class="label">Assing doctor</label>
              </div>
              <div class="inputContainer">
                <input type="text" class="input" placeholder="a">
                <label for="" class="label">Assing nurse</label>
              </div>
              <div class="inputContainer">
                <input type="text" class="input" placeholder="a">
                <label for="" class="label">Assing relative</label>
              </div>
            </form>
          </div>
      </template>
    
      <script>
     
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
        box-shadow: 0 10px 25px rgba(92, 99, 105, .2);
      }
      .title {
        font-family:Georgia, 'Times New Roman', Times, serif;
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
        color:black;
        background-color: beige;
        font-size: 16px;
        transition: 0.5s;
        z-index: 0;
      }
    
      .input:focus + .label {
        top: -7px;
        left: 3px;
        z-index: 10;
        font-size: 14px;
        font-weight: 600;
        color: purple;
      }
      </style>