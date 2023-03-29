<?php require('./layout/header.php') ?>
    
    <?php require('./layout/aside.php') ?>

    <section >
    <h1 class="titulo__formulario">Registro de Material</h1> 
            
            <div class="registro-material">
              
                <div class="bloque1">
                    <label for="seleccionar-material">Seleccione:</label>
                    <select id="seleccionar" required>
                    <option value="" selected disabled >Seleccione Material</option>
                    <option value="Cedula de ciudadania"required>Carbon</option>
                    <option value="Nit" required>Acero Inoxidable</option>
                    <option value="Cedula de extranjera" required>Madera</option>
                    <option value="Pasaporte" required>Hierro</option>
                   </select>
                
                    <label for="Diseño-Material">Seleccione:</label>
                   <select id="seleccionar" required> 
                    <option value="" selected disabled >Diseño de material</option>
                    <option value="Cedula de ciudadania">Diseño 1</option>
                    <option value="Nit">Diseño 2</option>
                    <option value="Cedula de extranjera">Diseño 3</option>
                    <option value="Pasaporte">Diseño 4</option>
                    </select>
                </div>
        
    
                <!-- Bloque 2 -->
                <div class="bloque2">
                    
                    <div class="caja">
                      <label for="Calibre">Calibre:</label>
                      <input class="caja__input" type="number" required>
                    </div>   
               
                    <div class="caja">
                        <label for="Medidas">Medidas:</label>
                        <input class="caja__input" type="number" required>
                    </div>
    
                    <div class="caja">
                        <label for="mt-cm">Seleccione:</label>
                        <select id="seleccionar1" required> 
                           <option value="" selected disabled >MT</option>
                           <option value="Cedula de ciudadania">MT</option>
                           <option value="Nit">CM</option>
                        </select>
                    </div>
                    
                    <div class="caja">
                        <label for="Pulgada">Pulgadas:</label>
                        <input class="caja__input" type="number" required>
                    </div>
    
    
                </div>
                <!-- ------------------- -->
    
                <!-- Bloque 3 -->
                <div class="bloque3">
                    
                   <div class="left">
                       <label for="Compra">Valor de Compra:</label>
                       <input id="compra" class="control6" name="numeros" pattern="[0-9]+" required>
                   </div>
               
                   <div class="left">
                       <label for="Venta">Valor de Venta:</label>
                       <input id="Venta" class="control6" name="numeros" pattern="[0-9]+" required>
                   </div>
               </div>
               <!-- -------------------------------------- -->
               
               <!-- COMENTARIOS -->
                <div class="comentarios">
                    <textarea name="mensaje" placeholder="comentarios"></textarea>
                </div>
               
                
                <div class="boton-guardar">
                    <input type="submit" name="Guardar" value="Guardar" class="guardar" >
                </div>
                
               <!-- --------- -->
    
            </div>   
    </section>


    
<?php require('./layout/footer.php') ?>