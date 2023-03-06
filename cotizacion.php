<?php require('./layout/header.php') ?>
    
    <?php require('./layout/aside.php') ?>

    <main class="cotizacion-main">
        
    <h1 class="quote-h1"">Cotización</h1>
    <table class="quote-cotizacion-1">
        <tr>
            <td>
                <label for="">Cedula</label>
                <input type="number" name="" id="">
            </td>
            <td>
                <label for="">Nombre</label><br>
                <input type="text">
            </td>
            <td>
                <label for="">Telefono</label>
                <input type="number">
            </td>
            <td>
                <label for="">Direccion</label>
                <input type="text" name="" id="">
            </td>
            <td>
                <label for="">Email</label>
                <input type="text">
            </td>
            
            <tr>
                <td>Datos de cotizacion:</td>
            </tr>
            <tr>
                <td>
                    <label for="">Fecha</label>
                    <input type="date" name="" id="">
                </td>
                <td>
                    <label for="">Numero de cotizacion</label>
                    <input type="number" name="" id="">
                </td>
                <td>
                    <label for="">Elaborado por</label>
                    <input type="text" name="" id="">
                </td>
            </tr>
        </tr>
    </table>
    <table class="table-quote-2">
        <tr>
            <th>Tipo</th>
            <th>Materiales</th>
            <th>Diseño</th>
            <th>Descripción</th>
            <th>Cantidad</th>
            <th>Valor unidad</th>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </table>
    </main>

      
<?php require('./layout/footer.php') ?>