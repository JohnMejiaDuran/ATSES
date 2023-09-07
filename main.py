from flask import Flask, request, render_template
from conectar import * #Importando conexion BD


app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/registrocliente', methods=['GET', 'POST'])
def registrarForm():
    msg =''
    if request.method == 'POST':
        nombres             = request.form['nombres']
        apellidos           = request.form['apellidos']
        t_documento         = request.form['t_documento']
        id_cliente          = request.form['id_cliente']
        t_de_Persona        = request.form['t_de_persona']
        contacto            = request.form['contacto']
        email               = request.form['email']
        ciudad              = request.form['ciudad']
        dirección           = request.form['direccion']
            
        conexion_MySQLdb = conexionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute('INSERT INTO clientes(nombres, apellidos, t_documento, id_cliente, t_de_Persona, contacto, email, ciudad, direccion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', ( nombres , apellidos, t_documento, id_cliente, t_de_Persona, contacto, email, ciudad, dirección))
            
            
        # sql         = ("INSERT INTO administradores(cedula, nombre, correo, celular, usuario, contrasena) VALUES (%s, %s, %s, %s, %s, %s)")
        # valores     = (cedula,nombre,correo,celular,usuario,contrasena)
        # cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        msg = 'Registro con exito'
        
        print(cursor.rowcount, "registro insertado")
        print("1 registro insertado, id", cursor.lastrowid)
  
        return render_template('registrocliente.html', msg='Cliente Registrado')
    else:
        return render_template('registrocliente.html', msg = 'Metodo HTTP incorrecto')

@app.route('/actualizacion_cliente')
def actualizarcliente():
    msg =''
    if request.method == 'POST':
        nombres             = request.form['nombres']
        apellidos           = request.form['apellidos']
        t_documento         = request.form['t_documento']
        id_cliente          = request.form['id_cliente']
        t_de_Persona        = request.form['t_de_persona']
        contacto            = request.form['contacto']
        email               = request.form['email']
        ciudad              = request.form['ciudad']
        dirección           = request.form['direccion']
            
        conexion_MySQLdb = conexionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute('INSERT INTO actualizacion_cliente(nombres, apellidos, t_documento, id_cliente, t_de_Persona, contacto, email, ciudad, direccion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', ( nombres , apellidos, t_documento, id_cliente, t_de_Persona, contacto, email, ciudad, dirección))
            
        conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        msg = 'Registro con exito'
        
        print(cursor.rowcount, "registro insertado")
        print("1 registro insertado, id", cursor.lastrowid)
  
        return render_template('actualizarcliente.html', msg='Cliente Actualizado')
    else:
        return render_template('actualizarcliente.html', msg = 'Metodo HTTP incorrecto')

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores.html')

@app.route('/registroproveedor', methods=['GET', 'POST'])
def registrar_proveedores():
    msg =''
    if request.method == 'POST':
        nombre              = request.form['nombre']
        t_documento         = request.form['t_documento']
        id_proveedor        = request.form['id_proveedor']
        t_de_Persona        = request.form['t_de_persona']
        direccion           = request.form['direccion']
        contacto            = request.form['contacto']
        email               = request.form['email']
        ciudad              = request.form['ciudad']
       
            
        conexion_MySQLdb = conexionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute('INSERT INTO proveedores(nombre, t_documento, id_proveedor, t_de_Persona, direccion, contacto, email, ciudad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (nombre, t_documento, id_proveedor, t_de_Persona, direccion, contacto, email, ciudad))
            
        conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        msg = 'Registro con exito'
        
        print(cursor.rowcount, "registro insertado")
        print("1 registro insertado, id", cursor.lastrowid)
  
        return render_template('registroproveedor.html', msg='Proveedor Registrado')
    else:
        return render_template('registroproveedor.html', msg = 'Metodo HTTP incorrecto')
    
@app.route('/actualizarproveedor')
def actualizarproveedor():
    return render_template('actualizarproveedor.html')

@app.route('/estructuras')
def estructuras():
    return render_template('estructuras.html')

@app.route('/registroestructuras')
def registroestructuras():
    return render_template('registroestructuras.html')

@app.route('/actualizarestructura')
def actualizarestructura():
    return render_template('actualizarestructura.html')

@app.route('/materiales')
def materiales():
    return render_template('materiales.html')

@app.route('/registromaterial')
def registromaterial():
    return render_template('registromaterial.html')

@app.route('/actualizarmaterial')
def actualizarmaterial():
    return render_template('actualizarmaterial.html')

@app.route('/cotizacion')
def cotizacion():
    return render_template('cotizacion.html')


if __name__ == '__main__': 
    app.run(debug=True, host='localhost', port=5500)