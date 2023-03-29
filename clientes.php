<?php require('./layout/header.php') ?>
    
    <?php require('./layout/aside.php') ?>

    <section class="container__clientes">
        <div class="clientes">
            <div class="formulario__clientes">
                <h1 class="titulo__formulario">Base de datos Clientes</h1>
                
            </div>
            <h3 class="titulo1">Resgitre los datos básicos de clientes. </h3>
            <div class="base2">
            <div class="tabla">
                <label for="#documento" class="colocar_documento">Número de Documento<span class="span">*</span></label>
                <input type="text" name="introducir_Cedula o Nit" id="Cedula o Nit" required="obligatorio" placeholder="Cedula o Nit">
           </div>
            <div class="tabla1">
                <button class="button__buscar" type="submit" name="enviar_formulario" id="Buscar"><a class="Buscar">Buscar</a></button>
            </div>
            <div>
                <button class="button__add">
                    <a href="http://localhost/ATSES/registrocliente.php"><i class="fa-solid fa-plus" style="color: #ffffff;">&nbsp;</i>Añadir</a>
                </button>
                
            </div>
        </div>
        <table class="tablaclientes">
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>T. Documento</th>
                    <th>N° de Documento</th>
                    <th>T. de Persona</th>
                    <th>N° de Contacto</th>
                    <th>Email</th>
                    <th>Ciudad</th>
                    <th>Dirección</th>
                    <th>Opciones</th>  
                </tr>
          </thead>
          <tbody>
                <tr>
                    <td>Arturo Jose </td>
                    <td>prieto</td>
                    <td>cedula de ciudadania</td>
                    <td>23976327</td>
                    <td>Juridica</td>
                    <td>3145903867</td>
                    <td>arturo_prieto@hmail.com</td>
                    <td>Bucaramanga</td>
                    <td>crr. 20 # 23-45</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
                <tr>
                    <td>Maria Roberta </td>
                    <td>Acuña</td>
                    <td>cedula de ciudadania</td>
                    <td>23976327</td>
                    <td>Juridica</td>
                    <td>3145903867</td>
                    <td>arturo_prieto@hmail.com</td>
                    <td>Bucaramanga</td>
                    <td>crr. 20 # 23-45</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
                <tr>
                    <td>pedro </td>
                    <td>Sierra</td>
                    <td>cedula de ciudadania</td>
                    <td>23976327</td>
                    <td>Juridica</td>
                    <td>3145903867</td>
                    <td>arturo_prieto@hmail.com</td>
                    <td>Bucaramanga</td>
                    <td>crr. 20 # 23-45</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
                <tr>
                    <td>Fransisco Jose</td>
                    <td>Alvear Porras</td>
                    <td>cedula de ciudadania</td>
                    <td>23976327</td>
                    <td>Juridica</td>
                    <td>3145903867</td>
                    <td>arturo_prieto@hmail.com</td>
                    <td>Bucaramanga</td>
                    <td>crr. 20 # 23-45</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
                <tr>
                    <td>Sergio Andres </td>
                    <td>Pontes</td>
                    <td>cedula de ciudadania</td>
                    <td>23976327</td>
                    <td>Juridica</td>
                    <td>3145903867</td>
                    <td>arturo_prieto@hmail.com</td>
                    <td>Bucaramanga</td>
                    <td>crr. 20 # 23-45</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>  
          <tbody>
                <tr>
                    <td>Mario  </td>
                    <td>Rodriguez</td>
                    <td>cedula de ciudadania</td>
                    <td>23976327</td>
                    <td>Juridica</td>
                    <td>3145903867</td>
                    <td>arturo_prieto@hmail.com</td>
                    <td>Bucaramanga</td>
                    <td>crr. 20 # 23-45</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
                <tr>
                    <td>Fernando Jose</td>
                    <td>Flores Menco</td>
                    <td>cedula de ciudadania</td>
                    <td>23976327</td>
                    <td>Juridica</td>
                    <td>3145903867</td>
                    <td>arturo_prieto@hmail.com</td>
                    <td>Bucaramanga</td>
                    <td>crr. 20 # 23-45</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
                <tr>
                    <td>Alcides Jabier</td>
                    <td>Toloza Diaz</td>
                    <td>cedula de ciudadania</td>
                    <td>23976327</td>
                    <td>Juridica</td>
                    <td>3145903867</td>
                    <td>arturo_prieto@hmail.com</td>
                    <td>Bucaramanga</td>
                    <td>crr. 20 # 23-45</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
                <tr>
                    <td>Rolando Luis</td>
                    <td>Peinado Castañeda</td>
                    <td>cedula de ciudadania</td>
                    <td>23976327</td>
                    <td>Juridica</td>
                    <td>3145903867</td>
                    <td>arturo_prieto@hmail.com</td>
                    <td>Bucaramanga</td>
                    <td>crr. 20 # 23-45</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>  
       </table>
       <div class="tabla1">
            <button class="button__guardar" type="submit" name="enviar_formulario" id="Guardar"><a class="Guardar">Guardar</a></button>
        </div>
      </div>
  </div>
        </section>

    
<?php require('./layout/footer.php') ?>