<?php require('./layout/header.php') ?>
    
    <?php require('./layout/aside.php') ?>

    <section class="container__clientes">
        <div class="clientes">
            <div class="formulario__clientes">
                <h1 class="titulo__formulario">Estructuras</h1>
                
            </div>
            <div class="tabla__nav">

                <div class="tabla">
                    <label for="#documento" class="tabla__documento">Código o nombre<span class="span">*</span></label>
                    <input class="tabla__input"type="text" name="introducir_Cedula o Nit" id="Cedula o Nit" required="obligatorio" placeholder="Código o nombre">
                    <div class="icon__search">

                        <a  href=""><i  class=" fa-solid fa-magnifying-glass"></i></a>
                    </div>
                </div>
            
                <div class="tabla__button-nav">
                    <button class="button__add">
                        <a href="http://localhost/ATSES/registroestructuras.php"><i class="fa-solid fa-plus" style="color: #ffffff;">&nbsp;</i>Añadir</a>
                    </button>
                </div>
            </div>
        <table class="tablaclientes">
            <thead>
                <tr>
                    <th>Estructura</th>
                    <th>Diseño</th>
                    <th>Medidas</th>
                    <th>Material</th>
                    <th>Valor venta</th>
                    <th>Opciones</th>  
                </tr>
          </thead>
          <tbody>
                <tr>
                    <td>Puerta</td>
                    <td>3D</td>
                    <td>2x5</td>
                    <td>Acero</td>
                    <td>1.200.000</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
          <tr>
                    <td>Puerta</td>
                    <td>3D</td>
                    <td>2x5</td>
                    <td>Acero</td>
                    <td>1.200.000</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
          <tr>
                    <td>Puerta</td>
                    <td>3D</td>
                    <td>2x5</td>
                    <td>Acero</td>
                    <td>1.200.000</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
          <tr>
                    <td>Puerta</td>
                    <td>3D</td>
                    <td>2x5</td>
                    <td>Acero</td>
                    <td>1.200.000</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
          <tr>
                    <td>Puerta</td>
                    <td>3D</td>
                    <td>2x5</td>
                    <td>Acero</td>
                    <td>1.200.000</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>  
          <tbody>
                <tr>
                    <td>Puerta</td>
                    <td>3D</td>
                    <td>2x5</td>
                    <td>Acero</td>
                    <td>1.200.000</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
                <tr>
                    <td>Puerta</td>
                    <td>3D</td>
                    <td>2x5</td>
                    <td>Acero</td>
                    <td>1.200.000</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
                <tr>
                    <td>Puerta</td>
                    <td>3D</td>
                    <td>2x5</td>
                    <td>Acero</td>
                    <td>1.200.000</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
                <tr>
                    <td>Puerta</td>
                    <td>3D</td>
                    <td>2x5</td>
                    <td>Acero</td>
                    <td>1.200.000</td>
                    <td><a href="http://localhost/ATSES/actualizarcliente.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>  
       </table>
       <div class="guardar">
            <button class="guardar__button" type="submit" name="enviar_formulario" id="Guardar"><a class="Guardar">Guardar</a></button>
        </div>
      </div>
  </div>
        </section>

    
<?php require('./layout/footer.php') ?>