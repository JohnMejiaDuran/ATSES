<?php require('./layout/header.php') ?>
    
    <?php require('./layout/aside.php') ?>


<<<<<<< HEAD
        <section> 
                <div class="cotizacion__titulo">
                    <h1 class="titulo__formulario">Cotizacion</h1>
                </div>
                <div class="cotizaciones__contenedor">
                    
                    <div class="cotizacion__cedula">
                        <label for="">Cedula</label>
                        <input class="input__cedula"type="text" placeholder="Cedula o Nit">
                        <a  href=""><i  class=" fa-solid fa-magnifying-glass"></i></a>
                    </div>
                    <div class="cotizacion__nombre">
                        <label for="">Nombre</label>
                        <input type="text" placeholder="Nombre">
                    </div>
                    <div class="cotizacion__telefono">
                        <label for="">Telefono</label>
                        <input type="text" placeholder="Telefono">
                    </div>
                    <div class="cotizacion__direccion">
                        <label for="">Direccion</label>
                        <input type="text" placeholder="Direccion">
                    </div>
                    <div class="cotizacion__email">
                        <label for="">E-mail</label>
                        <input type="text" placeholder="E-mail">
                    </div>
                    <div class="cotizacion__fecha">
                        <label for="">Fecha</label>
                        <input type="date" placeholder="Fecha">
                    </div>
                    <div class="cotizacion__numero">
                        <label for=""># cotizacion</label>
                        <input type="text" placeholder="# de Cotizacion">
                    </div>
                    <div class="cotizacion__elaborado">
                        <label for="">Elaborado por</label>
                        <input type="text" placeholder="Elaborado por">
                    </div>
                </div>
=======
        <section class="section__cotizacion"> 
            <div>
                <h1 class="titulo__formulario">Cotizacion</h1>
            </div>
        <article>
          
            <div class="otrovalor">
            
                <div>
                    <label for="">Cedula o Nit</label>
                    <input type="text">
                </div>
                <div>
                    <label for="">Nombre</label>
                    <input type="text">
                </div>
                <div>
                    <label for="">Telefono</label>
                    <input type="text">
                </div>
                <div>
                    <label for="">Dirección</label>
                    <input type="text">
                </div>
                <div>
                    <label for="">Email</label>
                    <input type="text">
                </div>
                <div>
                    <label for="">Mano de obra aluminero</label>
                    <input type="text">
                </div>
                <div>
                    <label for="">Valor total de cotizacion</label>
                    <input type="text">
                </div>  
            </div>
        </article>
>>>>>>> b02d151ecb6727f89e2221c2eaa4a26fe8b16d33
                    <div class="tabla__cotizacion">
                        <table  >
                            <thead>

                               <th>Tipo</th>
                                <th>Material</th>
                                <th>Diseño</th>
                                <th>Descripcion</th>
                                <th>Cantidad</th>
                                <th>Valor unidad</th> 
                                <th>Opciones</th>
                            </thead>
                            <tbody>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Puerta</option>
                                        <option value="">Ventana</option>
                                        <option value="">Porton Normal</option>
                                        <option value="">Porton electrico</option>
                                        <option value="">Rejas</option>
                                        <option value="">Pasamanos</option>
                                        <option value="">Escalaera</option>
                                        <option value="">Domos</option>
                                    </select>
                                </td>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Acero</option>
                                        <option value="">Aluminio</option>
                                        <option value="">PVC</option>
                                        <option value="">Vidrio</option>
                                        <option value="">Madera</option>
                                    </select>
                                </td>  
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">3D</option>
                                        <option value="">Lisas</option>
                                        <option value="">Geometricas</option>
                                        <option value="">Diseño personalizado</option>
                                        <option value="">Figuras</option>
                                        
                                    </select>
                                </td>        
                                <td>
                                    <input class="cotizacion__input" type="text">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                <a href=""><i class="fa-solid fa-trash" style="color: red;"></i></a>
                                <a href=""><i class="fa-solid fa-pen-to-square"></i></a>
                                </td>
                            </tbody>
                            <tbody>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Puerta</option>
                                        <option value="">Ventana</option>
                                        <option value="">Porton Normal</option>
                                        <option value="">Porton electrico</option>
                                        <option value="">Rejas</option>
                                        <option value="">Pasamanos</option>
                                        <option value="">Escalaera</option>
                                        <option value="">Domos</option>
                                    </select>
                                </td>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Acero</option>
                                        <option value="">Aluminio</option>
                                        <option value="">PVC</option>
                                        <option value="">Vidrio</option>
                                        <option value="">Madera</option>
                                    </select>
                                </td>  
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">3D</option>
                                        <option value="">Lisas</option>
                                        <option value="">Geometricas</option>
                                        <option value="">Diseño personalizado</option>
                                        <option value="">Figuras</option>
                                        
                                    </select>
                                </td>        
                                <td>
                                    <input class="cotizacion__input" type="text">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                <a href=""><i class="fa-solid fa-trash" style="color: red;"></i></a>
                                <a href=""><i class="fa-solid fa-pen-to-square"></i></a>
                                </td>
                            </tbody>
                            <tbody>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Puerta</option>
                                        <option value="">Ventana</option>
                                        <option value="">Porton Normal</option>
                                        <option value="">Porton electrico</option>
                                        <option value="">Rejas</option>
                                        <option value="">Pasamanos</option>
                                        <option value="">Escalaera</option>
                                        <option value="">Domos</option>
                                    </select>
                                </td>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Acero</option>
                                        <option value="">Aluminio</option>
                                        <option value="">PVC</option>
                                        <option value="">Vidrio</option>
                                        <option value="">Madera</option>
                                    </select>
                                </td>  
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">3D</option>
                                        <option value="">Lisas</option>
                                        <option value="">Geometricas</option>
                                        <option value="">Diseño personalizado</option>
                                        <option value="">Figuras</option>
                                        
                                    </select>
                                </td>        
                                <td>
                                    <input class="cotizacion__input" type="text">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                <a href=""><i class="fa-solid fa-trash" style="color: red;"></i></a>
                                <a href=""><i class="fa-solid fa-pen-to-square"></i></a>
                                </td>
                            </tbody>
                            <tbody>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Puerta</option>
                                        <option value="">Ventana</option>
                                        <option value="">Porton Normal</option>
                                        <option value="">Porton electrico</option>
                                        <option value="">Rejas</option>
                                        <option value="">Pasamanos</option>
                                        <option value="">Escalaera</option>
                                        <option value="">Domos</option>
                                    </select>
                                </td>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Acero</option>
                                        <option value="">Aluminio</option>
                                        <option value="">PVC</option>
                                        <option value="">Vidrio</option>
                                        <option value="">Madera</option>
                                    </select>
                                </td>  
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">3D</option>
                                        <option value="">Lisas</option>
                                        <option value="">Geometricas</option>
                                        <option value="">Diseño personalizado</option>
                                        <option value="">Figuras</option>
                                        
                                    </select>
                                </td>        
                                <td>
                                    <input class="cotizacion__input" type="text">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                <a href=""><i class="fa-solid fa-trash" style="color: red;"></i></a>
                                <a href=""><i class="fa-solid fa-pen-to-square"></i></a>
                                </td>
                            </tbody>
                            <tbody>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Puerta</option>
                                        <option value="">Ventana</option>
                                        <option value="">Porton Normal</option>
                                        <option value="">Porton electrico</option>
                                        <option value="">Rejas</option>
                                        <option value="">Pasamanos</option>
                                        <option value="">Escalaera</option>
                                        <option value="">Domos</option>
                                    </select>
                                </td>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Acero</option>
                                        <option value="">Aluminio</option>
                                        <option value="">PVC</option>
                                        <option value="">Vidrio</option>
                                        <option value="">Madera</option>
                                    </select>
                                </td>  
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">3D</option>
                                        <option value="">Lisas</option>
                                        <option value="">Geometricas</option>
                                        <option value="">Diseño personalizado</option>
                                        <option value="">Figuras</option>
                                        
                                    </select>
                                </td>        
                                <td>
                                    <input class="cotizacion__input" type="text">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                <a href=""><i class="fa-solid fa-trash" style="color: red;"></i></a>
                                <a href=""><i class="fa-solid fa-pen-to-square"></i></a>
                                </td>
                            </tbody>
                            <tbody>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Puerta</option>
                                        <option value="">Ventana</option>
                                        <option value="">Porton Normal</option>
                                        <option value="">Porton electrico</option>
                                        <option value="">Rejas</option>
                                        <option value="">Pasamanos</option>
                                        <option value="">Escalaera</option>
                                        <option value="">Domos</option>
                                    </select>
                                </td>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Acero</option>
                                        <option value="">Aluminio</option>
                                        <option value="">PVC</option>
                                        <option value="">Vidrio</option>
                                        <option value="">Madera</option>
                                    </select>
                                </td>  
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">3D</option>
                                        <option value="">Lisas</option>
                                        <option value="">Geometricas</option>
                                        <option value="">Diseño personalizado</option>
                                        <option value="">Figuras</option>
                                        
                                    </select>
                                </td>        
                                <td>
                                    <input class="cotizacion__input" type="text">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                <a href=""><i class="fa-solid fa-trash" style="color: red;"></i></a>
                                <a href=""><i class="fa-solid fa-pen-to-square"></i></a>
                                </td>
                            </tbody>
                            <tbody>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Puerta</option>
                                        <option value="">Ventana</option>
                                        <option value="">Porton Normal</option>
                                        <option value="">Porton electrico</option>
                                        <option value="">Rejas</option>
                                        <option value="">Pasamanos</option>
                                        <option value="">Escalaera</option>
                                        <option value="">Domos</option>
                                    </select>
                                </td>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                    <option value=""></option>
                                        <option value="">Acero</option>
                                        <option value="">Aluminio</option>
                                        <option value="">PVC</option>
                                        <option value="">Vidrio</option>
                                        <option value="">Madera</option>
                                    </select>
                                </td>  
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                        <option value=""></option>
                                        <option value="">3D</option>
                                        <option value="">Lisas</option>
                                        <option value="">Geometricas</option>
                                        <option value="">Diseño personalizado</option>
                                        <option value="">Figuras</option>
                                        
                                    </select>
                                </td>        
                                <td>
                                    <input class="cotizacion__input" type="text">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                <a href=""><i class="fa-solid fa-trash" style="color: red;"></i></a>
                                <a href=""><i class="fa-solid fa-pen-to-square"></i></a>
                                </td>
                            </tbody>
                            <tbody>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                        <option value=""></option>
                                        <option value="">Puerta</option>
                                        <option value="">Ventana</option>
                                        <option value="">Porton Normal</option>
                                        <option value="">Porton electrico</option>
                                        <option value="">Rejas</option>
                                        <option value="">Pasamanos</option>
                                        <option value="">Escalaera</option>
                                        <option value="">Domos</option>
                                    </select>
                                </td>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                        <option value=""></option>
                                        <option value="">Acero</option>
                                        <option value="">Aluminio</option>
                                        <option value="">PVC</option>
                                        <option value="">Vidrio</option>
                                        <option value="">Madera</option>
                                    </select>
                                </td>  
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                        <option value=""></option>
                                        <option value="">3D</option>
                                        <option value="">Lisas</option>
                                        <option value="">Geometricas</option>
                                        <option value="">Diseño personalizado</option>
                                        <option value="">Figuras</option>
                                        
                                    </select>
                                </td>        
                                <td>
                                    <input class="cotizacion__input" type="text">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                <a href=""><i class="fa-solid fa-trash" style="color: red;"></i></a>
                                <a href=""><i class="fa-solid fa-pen-to-square"></i></a>
                                </td>
                            </tbody>
                            <tbody>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                        <option value=""></option>
                                        <option value="">Puerta</option>
                                        <option value="">Ventana</option>
                                        <option value="">Porton Normal</option>
                                        <option value="">Porton electrico</option>
                                        <option value="">Rejas</option>
                                        <option value="">Pasamanos</option>
                                        <option value="">Escalaera</option>
                                        <option value="">Domos</option>
                                    </select>
                                </td>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                        <option value=""></option>
                                        <option value="">Acero</option>
                                        <option value="">Aluminio</option>
                                        <option value="">PVC</option>
                                        <option value="">Vidrio</option>
                                        <option value="">Madera</option>
                                    </select>
                                </td>  
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                        <option value=""></option>
                                        <option value="">3D</option>
                                        <option value="">Lisas</option>
                                        <option value="">Geometricas</option>
                                        <option value="">Diseño personalizado</option>
                                        <option value="">Figuras</option>
                                        
                                    </select>
                                </td>        
                                <td>
                                    <input class="cotizacion__input" type="text">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                <a href=""><i class="fa-solid fa-trash" style="color: red;"></i></a>
                                <a href=""><i class="fa-solid fa-pen-to-square"></i></a>
                                </td>
                            </tbody>
                            <tbody>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                        <option value=""></option>
                                        <option value="">Puerta</option>
                                        <option value="">Ventana</option>
                                        <option value="">Porton Normal</option>
                                        <option value="">Porton electrico</option>
                                        <option value="">Rejas</option>
                                        <option value="">Pasamanos</option>
                                        <option value="">Escalaera</option>
                                        <option value="">Domos</option>
                                    </select>
                                </td>
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                        
                                    <option value=""></option>
                                        <option value="">Acero</option>
                                        <option value="">Aluminio</option>
                                        <option value="">PVC</option>
                                        <option value="">Vidrio</option>
                                        <option value="">Madera</option>
                                    </select>
                                </td>  
                                <td>
                                    <select name="" id="" class="cotizacion__input">
                                        <option value=""></option>
                                        <option value="">3D</option>
                                        <option value="">Lisas</option>
                                        <option value="">Geometricas</option>
                                        <option value="">Diseño personalizado</option>
                                        <option value="">Figuras</option>
                                        
                                    </select>
                                </td>        
                                <td>
                                    <input class="cotizacion__input" type="text">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                    <input class="cotizacion__input" type="number">
                                </td>
                                <td>
                                <a href=""><i class="fa-solid fa-trash" style="color: red;"></i></a>
                                <a href=""><i class="fa-solid fa-pen-to-square"></i></a>
                                </td>
                            </tbody>
                            
                        </table>
                    </div>
                    <article>
<<<<<<< HEAD

            <div class="otrovalor">
                <fieldset>
                        <legend>Otros valores</legend>
                    <div>
                        <label for="">Valor materiales</label>
                        <input type="text">
                    </div>
                    <div>
                        <label for="">Mano de obra</label>
                        <input type="text">
                    </div>
                    <div>
                        <label for="">Mano de obra menos 40%</label>
                        <input type="text">
                    </div>
                    <div>
                        <label for="">Materiales en empresa</label>
                        <input type="text">
                    </div>
                    <div>
                        <label for="">AIU</label>
                        <input type="text">
                    </div>
                    <div>
                        <label for="">Mano de obra aluminero</label>
                        <input type="text">
                    </div>
                    <div>
                        <label for="">Valor total de cotizacion</label>
                        <input type="text">
                    </div>
                     
                
                </fieldset>
                <div class="guardar">
                    <button class="guardar__button" type="submit" name="enviar_formulario" id="Guardar"><a class="Guardar">Guardar</a></button>
                

                        <button style="background-color:#26004b ; margin-left: 10px;" class="guardar__button" type="submit" name="enviar_formulario" id="Guardar"><a class="Guardar">Imprimir</a></button>
                    </div>
                </div> 
            </div>
        </article>
                  
        </section>
        
=======
<h3>Otros valores</h3>
<div class="otrovalor">

<div>
    <label for="">Valor materiales</label>
     <input type="text">
</div>
<div>
    <label for="">Mano de obra</label>
     <input type="text">
</div>
<div>
    <label for="">Mano de obra menos 40%</label>
     <input type="text">
</div>
<div>
    <label for="">Materiales en empresa</label>
     <input type="text">
</div>
<div>
    <label for="">AIU</label>
     <input type="text">
</div>
<div>
    <label for="">Mano de obra aluminero</label>
     <input type="text">
</div>
<div>
    <label for="">Valor total de cotizacion</label>
     <input type="text">
</div>
<div class="button__cotizacion">
    <button>
        <a href="">Guardar</a>
    </button>
</div>    
</div>
</article>
        </section>
   
>>>>>>> b02d151ecb6727f89e2221c2eaa4a26fe8b16d33
        

<?php require('./layout/footer.php') ?>