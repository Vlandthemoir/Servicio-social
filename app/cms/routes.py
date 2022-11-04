from flask import render_template,request,redirect,url_for
from flask_mysqldb import MySQL 
from . import cms
from app import db

def com():
    com = db.connection.commit()
    return com

def cur():
    cur = db.connection.cursor()
    return cur

def deleteRow(id,table,field):
    cur().execute('DELETE FROM '+table+' WHERE '+field+' = {0}'.format(id))
    com()
    return print("all is ok")

def query(table):
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM "+table)
    result = cur.fetchall()
    return result

def querySpecific(table,condition):
    cur().execute("SELECT * FROM "+table+" WHERE "+condition);
    result = cur().fetchall()
    return result

@cms.route('/login')
def login():
    return render_template('cms_login.html')

@cms.route('/verano')
def verano():
    return render_template('cms_verano.html', verano = query("taller_verano"))

@cms.route('/verano/add',methods=['POST'])
def add_verano():
    if request.method == 'POST':
        id = 0
        nombre = request.form['nombre']
        portada = request.form['portada']
        dias = request.form['dias']
        horario = request.form['horario']
        edades = request.form['edades']
        cur().execute('INSERT INTO taller_verano (id,nombre,imagen,dias,horario,edades) VALUES (%s,%s,%s,%s,%s,%s)',(id,nombre,portada,dias,horario,edades))
        com()
        return redirect(url_for('cms.verano'))

@cms.route('/verano/update/<id>',methods=['POST','GET'])
def update_verano():
    return redirect(url_for('cms.verano'))

@cms.route('/verano/delete/<id>',methods=['POST','GET'])
def delete_verano(id):
    deleteRow(id,"taller_verano","id")
    return redirect(url_for('cms.verano'))

@cms.route('/permanente')
def permanente():
    return render_template('cms_permanente.html', permanente = query("taller_permanente"))

@cms.route('/permanente/add',methods=['POST'])
def add_permanente():
    if request.method == 'POST':
        id = 0
        nombre = request.form['nombre']
        portada = request.form['portada']
        dias = request.form['dias']
        horario = request.form['horario']
        edades = request.form['edades']
        cur().execute('INSERT INTO taller_permanente (id,nombre,imagen,dias,horario,edades) VALUES (%s,%s,%s,%s,%s,%s)',(id,nombre,portada,dias,horario,edades))
        com()
        return redirect(url_for('cms.permanente'))

@cms.route('/permanente/update/<id>',methods=['POST','GET'])
def update_permanente(id): 
    return redirect(url_for('cms.permanente'))

@cms.route('/permanente/delete/<id>',methods=['POST','GET'])
def delete_permanente(id):
    deleteRow(id,"taller_permanente","id")
    return redirect(url_for('cms.permenente'))

@cms.route('/galeria')
def galeria():
    return render_template('cms_galeria.html', galeria = query("galeria"))

@cms.route('/galeria/add',methods=['POST'])
def add_galeria():
    if request.method == 'POST':
        id = 0
        titulo = request.form['titulo']
        portada = request.form['portada']
        fecha = request.form['fecha']
        autor = request.form['autor']
        descripcion = request.form['descripcion']
        cur().execute('INSERT INTO galeria (id,titulo,imagen,fecha,autor,descripcion) VALUES (%s,%s,%s,%s,%s,%s)',(id,titulo,portada,fecha,autor,descripcion))
        com()
        return redirect(url_for('cms.galeria'))

@cms.route('galeria/update/<id>',methods=['POST','GET'])
def update_galeria():
    return redirect(url_for('cms.galeria'))

@cms.route('galeria/delete/<id>',methods=['POST','GET'])
def delete_galeria(id):
    deleteRow(id,"galeria","id")
    return redirect(url_for('cms.galeria'))
