from flask import Flask, request, render_template
from conectar import * #Importando conexion BD


app = Flask(__name__) 

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

@app.route('/registrocliente', methods=['GET', 'POST'])
def registrarForm():
    msg =''
    if request.method == 'POST':
        Nombres             = request.form['Nombres']
        Apellidos            = request.form['Apellidos']
        T_Documento         = request.form['T_Documento']
        id_cliente          = request.form['id_cliente']
        T_de_Persona        = request.form['T_de_persona']
        N_de_Contacto       = request.form['N_de_Contacto']
        Email               = request.form['Email']
        Ciudad              = request.form['Ciudad']
        Dirección           = request.form['Direccion']
            
        conexion_MySQLdb = conexionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute('INSERT INTO clientes(Nombre, Apellidos, T_Documento, id_cliente, T_de_Persona, N_de_Contacto, Email, Ciudad, Dirección) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', ( Nombres , Apellidos, T_Documento, id_cliente, T_de_Persona, N_de_Contacto, Email, Ciudad, Dirección))
            
            
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