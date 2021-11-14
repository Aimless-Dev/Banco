from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_DB'] = 'banco'
mysql = MySQL(app)

app.secret_key = "mysecretkey"

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    user = cur.fetchall()
    cur.execute('SELECT * FROM sucursal')
    sucu = cur.fetchall()
    cur.close()
    return render_template('index.html', user = user, suc = sucu)

@app.route('/add', methods=['POST'])
def add_registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        sexo = request.form['sexo']
        curp = request.form['curp'].upper()
        email = request.form['email']
        password = request.form['password']
        sucursal = request.form['sucursal']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (Nombre, Apellido, Curp, Sexo, Email, Pass, Sucursal) VALUES (%s, %s, %s, %s, %s, %s, %s)', (nombre, apellido, curp, sexo, email, password, sucursal))
        mysql.connection.commit()
        flash('Usuario registrado correctamente')
        return redirect(url_for('index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_data(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id = {0}'.format(id))
    data = cur.fetchall()
    cur.execute('SELECT * FROM sucursal')
    sucu = cur.fetchall()
    cur.close()
    return render_template('edit.html', data = data[0], suc = sucu)

@app.route('/update/<id>', methods = ['POST'])
def update_data(id):
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        sucursal = request.form['sucursal']

        cur = mysql.connection.cursor()
        cur.execute('UPDATE usuarios SET Email = %s, Pass = %s, Sucursal = %s WHERE id = %s', (email, password, sucursal, id))
        mysql.connection.commit()
        flash('Usuario actualizado correctamente')
        return redirect(url_for('index'))

@app.route('/delete/<id>', methods = ['POST', 'GET'])
def delete_data(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuarios WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Usuario eliminado correctamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=3000)