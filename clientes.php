<?php require('./layout/header.php') ?>
    
    <?php require('./layout/aside.php') ?>

    <section class="container__clientes">
        <div class="clientes">
            <div class="formulario__clientes">
                <h1 class="titulo__formulario">Base de datos Clientes y mas clientes</h1>
                
            </div>
            <div class="tabla__nav">

                <div class="tabla">
                    <label for="#documento" class="tabla__documento">Número de Documento<span class="span">*</span></label>
                    <input class="tabla__input"type="text" name="introducir_Cedula o Nit" id="Cedula o Nit" required="obligatorio" placeholder="Cedula o Nit">
                    <div class="icon__search">

                        <a  href=""><i  class=" fa-solid fa-magnifying-glass"></i></a>
                    </div>
                </div>
            
                <div class="tabla__button-nav">
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
       </table>
       
      </div>
  </div>
        </section>

    
<?php require('./layout/footer.php') ?>