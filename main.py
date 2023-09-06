from flask import Flask, request, render_template
from conectar import * #Importando conexion BD


app = Flask(__name__)



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
  
        return render_template('index.html', msg='Cliente Registrado')
    else:
        return render_template('index.html', msg = 'Metodo HTTP incorrecto')


if __name__ == '__main__': 
    app.run(debug=True, host='localhost', port=5500)