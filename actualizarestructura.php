<?php require('./layout/header.php') ?>
    
    <?php require('./layout/aside.php') ?>

    <section >
        <h1 class="titulo__formulario">Actualizar Estructuras</h1> 
            
            <div class="registro-material">
              
                <div class="bloque1">
                    <label for="seleccionar-material">Nombre de estructura</label>
                        <input class="caja__input"type="text" name="" id="">
                        
                
                    <label for="Diseño-Material">Diseño de estructura</label>
                    <input class="caja__input"type="text" name="" id="">
                        
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
                       <label for="Venta">Valor de Venta:</label>
                       <input class="caja__input"id="Venta" class="control6" name="numeros" pattern="[0-9]+" required>
                   </div>
               </div>
               <!-- -------------------------------------- -->
               
               <!-- COMENTARIOS -->
                <div class="comentarios">
                    <textarea name="mensaje" placeholder="comentarios"></textarea>
                </div>
               
                
                <div class="guardar">
                    <button class="guardar__button" type="submit" name="enviar_formulario" id="Guardar"><a class="Guardar">Actualizar</a></button>
                </div>
                
               <!-- --------- -->
    
            </div>   
    </section>


    
<?php require('./layout/footer.php') ?>