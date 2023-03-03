<?php require('./layout/header.php') ?>
    
    <?php require('./layout/aside.php') ?>

    <main>
        <section>
            <table>
                <thead>
                    <tr>
                        <th><h1>Cotizacion</h1></th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td><input type="number" placeholder="Cedula o Nit"></td>
                        <td><input type="text" placeholder="Nombre o razon social"></td>
                        <td><input type="number" placeholder="Telefono"></td>
                    </tr>
                    <tr>
                        <td><input type="text" placeholder="Dirección"></td>
                        <td><input type="email" placeholder="Email"></td>
                    </tr>
                    <tr>
                        <td><h2>Datos de cotizacion:</h2></td>
                    </tr>
                </tbody>
            
            </table>
        </section>
    </main>

      
<?php require('./layout/footer.php') ?>