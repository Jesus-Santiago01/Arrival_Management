from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)
conn = MySQLdb.connect(host="127.0.0.1",user="root",password="",db="arrival_management")
#MUESTA LA BASE
@app.route('/base')
def base():
    return render_template('base.html')
#MUESTA LA BASE2
@app.route('/base2')
def base2():
    return render_template('base2.html')
#MUESTA LA INTERFACE PRINCIPAL
@app.route('/')
def principal():
    return render_template('index.html')
#MUESTA EL LOGIN Y REGISTRO
@app.route('/login')
def login():
    return render_template('login.html')
#MUESTA LA VENTANA DE PROCESOS
@app.route('/process')
def process():
    return render_template('process.html')
#MUESTA LA VENTANA DE REPORTES
@app.route('/reports')
def reports():
    return render_template('reportes.html')
#MUESTA LA VENTANA DE ADMINISTRADORES
@app.route('/admin')
def admin():
    return render_template('administrador.html')

#METODO PARA REGISTRO DE USUARIOS
@app.route('/add_user' , methods=['POST'])
def add_user():

    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        apaterno = str(request.form['apaterno'])
        amaterno = str(request.form['amaterno'])
        turno = request.form['turno']
        usuario = str(request.form['usuario'])
        contraseña = str(request.form['contraseña'])

        cursor = conn.cursor()

        cursor.execute("INSERT INTO usuarios (nombre,apaterno,amaterno,turno,usuario,contraseña) VALUES (%s,%s,%s,%s,%s,%s)",(nombre,apaterno,amaterno,turno,usuario,contraseña))

        conn.commit()
        return redirect(url_for("login"))

#METODO PARA VALIDACION DE USUARIOS EN BD
@app.route('/check_user' , methods=['POST'])
def check_user():
    if request.method == 'POST':
        usuario = str(request.form['usuario'])
        contraseña = str(request.form['contraseña'])
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario='"+usuario+"'")
        user = cursor.fetchone()
        print(user)
        return "valido"

if __name__ == '__main__':
    app.run(debug=True)
