from flask import Flask, request, render_template
from conectar import * #Importando conexion BD


app = Flask(__name__)

@app.route('/registroproveedor')
def registroproveedor():
    return render_template('registroproveedor.html')

@app.route('/registroestructuras')
def registroestructuras():
    return render_template('registroestructuras.html')


@app.route('/registrocliente')
def registrocliente():
    return render_template('registrocliente.html')

@app.route('/actualizarproveedor')
def actualizarproveedor():
    return render_template('actualizarproveedor.html')


@app.route('/actualizarmaterial')
def actualizarmaterial():
    return render_template('actualizarmaterial.html')

@app.route('/actualizarestructura')
def actualizarestructura():
    return render_template('actualizarestructura.html')


@app.route('/estructuras')
def estructuras():
    return render_template('estructuras.html')
 

@app.route('/cotizacion')
def cotizacion():
    return render_template('cotizacion.html')


@app.route('/proveedores')
def proveedores():
    return render_template('proveedores.html')


@app.route('/registromaterial')
def registromaterial():
    return render_template('registromaterial.html')


@app.route('/materiales')
def materiales():
    return render_template('materiales.html')


@app.route('/registrocliente')
def registro_cliente():
    return render_template('registrocliente.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/') 
def inicio(): 
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/actualizarcliente')
def actualizar_cliente():
    return render_template('actualizarcliente.html')

@app.route('/form', methods=['GET', 'POST'])
def registrarForm():
    msg =''
    if request.method == 'POST':
        Nombre              = request.form[' Nombre ']
        Apellido            = request.form['Apellido']
        T_Documento         = request.form['T. Documento']
        id_cliente          = request.form['id_cliente']
        T_de_Persona        = request.form['T_de_persona']
        N_de_Contacto       = request.form['N_de_Contacto']
        Email               = request.form['Email']
        Ciudad              = request.form['Ciudad']
        Dirección           = request.form['Dirección']
        Opciones            = request.form['Opciones']  
            
        conexion_MySQLdb = conexionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute('INSERT INTO cliente (Nombre , Apellido, T_Documento, id_cliente, T_de_Persona, N_de_Contacto, Email, Ciudad, Dirección, Opciones) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', ( Nombre , Apellido, T_Documento, id_cliente, T_de_Persona, N_de_Contacto, Email, Ciudad, Dirección, Opciones))
            
            
        # sql         = ("INSERT INTO administradores(cedula, nombre, correo, celular, usuario, contrasena) VALUES (%s, %s, %s, %s, %s, %s)")
        # valores     = (cedula,nombre,correo,celular,usuario,contrasena)
        # cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        msg = 'Registro con exito'
        
        print(cursor.rowcount, "registro insertado")
        print("1 registro insertado, id", cursor.lastrowid)
  
        return render_template('index.html', msg='Cliente Registrado')
    else:
        return render_template('index.html', msg = 'Metodo HTTP incorrecto')


if __name__ == '__main__': 
    app.run(debug=True, host='localhost', port=5500)