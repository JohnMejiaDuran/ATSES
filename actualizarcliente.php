<?php require('./layout/header.php') ?>
    
    <?php require('./layout/aside.php') ?>

    <section class="container__registrocliente">
      <div class="contact_form">
          <div class="formulario">      
              <h1 class="titulo__formulario">Actualizar Clientes</h1>
          </div>
          
          <form action="" method="post">       
              <div class="columnas" >
                  <div>
                      <label for="nombre" class="colocar_nombre">Nombres<span class="obligatorio">*</span></label>
                      <input type="text" name="introducir_nombre" id="nombre" required="obligatorio" placeholder="Escribe tu Nombre">
                  </div>
                  <div>
                        <label for="Apellidos" class="colocar_nombre">Apellidos<span class="obligatorio">*</span></label>
                        <input type="text" name="introducir_Apellidos" id="Apellidos" required="obligatorio" placeholder="Escribe tu Apellido">
                  </div>
                  <div>
                      <label for="Documento" class="seleccionar">Tipo de Documento<span class="obligatorio">*</span></label>
                      <select  class="seleccion__cliente" id="Seleccionar">
                          <option value="Seleccionar"></option>
                          <option value="Cedula de ciudadania">Cedula de ciudadania</option>
                          <option value="Nit">Nit</option>
                          <option value="Cedula de Extrangeria">Cedula de Extrangeria</option>
                          <option value="Pasaporte">Pasaporte</option>
                      </select>
                  </div>
                  <div>
                      <label for="#documento" class="colocar_documento">Número de Documento<span class="obligatorio">*</span></label>
                        <input type="text" name="introducir_Cedula o Nit" id="Cedula o Nit" required="obligatorio" placeholder="Cedula o Nit">
                  </div>
              </div>
        
            <div class="columnas">
              <div>
                <label for="tipo de persona" class="colocar_tipo_persona">Tipo de Persona <span class="obligatorio">*</span></label>
                <select  class="seleccion" id="Seleccionar">
                  <option value="seleccional"></option>
                  <option value="Persona Natural">Persona Natural</option>
                  <option value="Persona Juridica">Persona Juridica</option>
                </select> 
              </div> 
              <div>
                <label for="telefone" class="colocar_telefono">Teléfono o Celular<span class="obligatorio">*</span></label>
                <input type="tel" name="introducir_telefono" id="telefono" placeholder="Escribe tu teléfono">
              </div> 
              <div>
                <label for="email" class="colocar_email">Email<span class="obligatorio">*</span></label>
                  <input type="email" name="introducir_email" id="email" required="obligatorio" placeholder="Escribe tu Email">
              </div>
              <div>
                <label for="Ciudad" class="colocar_Ciudad">Ciudad de residencia<span class="obligatorio">*</span></label>
                <input type="text" name="introducir_Ciudad" id="Ciudad" required="obligatorio" placeholder="Escribe Ciudad donde Reside">
              </div>    
              <div>
                <label for="Dirección" class="colocar_Dirección">Dirección donde Reside<span class="obligatorio">*</span></label>
                <input type="text" name="introducir_Dirección" id="Dirección" required="obligatorio" placeholder="Escribe Dirección de Residencia.">
              </div>   
            </div> 
            
            <div class="guardar">
              <button  class="guardar__button" type="submit" name="enviar_formulario" id="enviar"><a class="enviar">Actualizar</a></button>
            </div>
            
            <div class="aviso">
              <span class="obligatorio"> * </span>los campos son obligatorios.
            </div>          
          </form>
        </div>  
      </div>
    </section>

    
<?php require('./layout/footer.php') ?>