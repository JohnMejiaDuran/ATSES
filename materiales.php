<?php require('./layout/header.php') ?>
    
    <?php require('./layout/aside.php') ?>

    <section class="container__clientes">
        <div class="clientes">
            <div class="formulario__clientes">
                <h1 class="titulo__formulario">Materiales</h1>
                
            </div>
            <div class="tabla__nav">

                <div class="tabla">
                    <label for="#documento" class="tabla__documento">Código o Nombre<span class="span">*</span></label>
                    <input class="tabla__input"type="text" name="introducir_Cedula o Nit" id="Cedula o Nit" required="obligatorio" placeholder="Código o nombre">
                    <div class="icon__search">

                        <a  href=""><i  class=" fa-solid fa-magnifying-glass"></i></a>
                    </div>
                </div>
            
                <div class="tabla__button-nav">
                    <button class="button__add">
                        <a href="http://localhost/ATSES/registromaterial.php"><i class="fa-solid fa-plus" style="color: #ffffff;">&nbsp;</i>Añadir</a>
                    </button>
                </div>
            </div>
        <table class="tablaclientes">
            <thead>
                <tr>
                    <th>Material</th>
                    <th>Clasificacion</th>
                    <th>Diseño</th>
                    <th>Calibre</th>
                    <th>Pulgada</th>
                    <th>Medidas</th>  
                    <th>Valor compra</th>
                    <th>Valor venta</th>
                    <th>opciones</th>
                </tr>
          </thead>
          <tbody>
                <tr>
                    <td>Acero</td>
                    <td>Inoxidable</td>
                    <td>Redondo</td>
                    <td>18</td>
                    <td>3</td>
                    <td>6 metros</td>
                    <td>35.000</td>
                    <td>40.000</td>
                    <td><a href="http://localhost/ATSES/actualizarmaterial.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
          <tr>
                    <td>Acero</td>
                    <td>Inoxidable</td>
                    <td>Redondo</td>
                    <td>18</td>
                    <td>3</td>
                    <td>6 metros</td>
                    <td>35.000</td>
                    <td>40.000</td>
                    <td><a href="http://localhost/ATSES/actualizarmaterial.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
          <tr>
                    <td>Acero</td>
                    <td>Inoxidable</td>
                    <td>Redondo</td>
                    <td>18</td>
                    <td>3</td>
                    <td>6 metros</td>
                    <td>35.000</td>
                    <td>40.000</td>
                    <td><a href="http://localhost/ATSES/actualizarmaterial.php"><span class="fas fa-edit"></span></a></td>
                </tr>
          </tbody>
          <tbody>
          <tr>
                    <td>Acero</td>
                    <td>Inoxidable</td>
                    <td>Redondo</td>
                    <td>18</td>
                    <td>3</td>
                    <td>6 metros</td>
                    <td>35.000</td>
                    <td>40.000</td>
                    <td><a href="http://localhost/ATSES/actualizarmaterial.php"><span class="fas fa-edit"></span></a></td>
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